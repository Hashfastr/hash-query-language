from typing import TYPE_CHECKING, Optional, Union
from Hql.Operators.Database import Database
from Hql.Exceptions import HqlExceptions as hqle
import logging
import polars as pl

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Context import Context

# Polars to Kusto type mapping — extend as needed.
POLARS_TO_KUSTO: dict[type, str] = {
    pl.Utf8: "string",
    pl.String: "string",
    pl.Int8: "int",
    pl.Int16: "int",
    pl.Int32: "int",
    pl.Int64: "long",
    pl.UInt8: "int",
    pl.UInt16: "int",
    pl.UInt32: "int",
    pl.UInt64: "long",
    pl.Float32: "real",
    pl.Float64: "real",
    pl.Boolean: "bool",
    pl.Date: "datetime",
    pl.Datetime: "datetime",
    pl.Duration: "timespan",
}

class Kusto(Database):
    def __init__(self, config:dict, name:str='Kusto Database'):
        from azure.kusto.data import KustoClient, KustoConnectionStringBuilder

        # from Hql.Compiler import Kusto
        Database.__init__(self, config, name=name)
        
        conf = self.config.get('conf', {})
        if not conf:
            raise hqle.ConfigException('Kusto database given no config')

        self.verify_config(conf, ['database', 'cluster', 'client_id', 'client_secret', 'tenant_id'])
        self.database = conf['database']
        self.cluster = conf['cluster']
        self.client_id = conf['client_id']
        self.client_secret = conf['client_secret']
        self.tenant_id = conf['tenant_id']

        self.methods = []

        self.can_push = True

        kcsb_data = KustoConnectionStringBuilder.with_aad_application_key_authentication(
            self.cluster, self.client_id, self.client_secret, self.tenant_id
        )
        self.query_client = KustoClient(kcsb_data)

    def _table_exists(self, table: str) -> bool:
        kql = f".show tables | where TableName == '{table}'"
        response = self.query_client.execute(self.database, kql)
        return len(response.primary_results[0]) > 0

    def _resolve_kusto_type(self, polars_type: pl.DataType) -> str:
        for pl_type, kusto_type in POLARS_TO_KUSTO.items():
            if isinstance(polars_type, pl_type):
                return kusto_type
        return "string"

    def _create_table(self, table: str, schema: pl.Schema) -> None:
        columns = ", ".join(
            f"['{col}']: {self._resolve_kusto_type(dtype)}"
            for col, dtype in schema.items()
        )
        command = f".create table ['{table}'] ({columns})"
        self.query_client.execute(self.database, command)

    def ensure_table(self, table: str, schema: pl.Schema) -> None:
        if not self._table_exists(table):
            self._create_table(table, schema)

    def push(self, ctx: 'Context', **kwargs) -> bool:
        from azure.kusto.ingest import IngestionProperties, QueuedIngestClient
        from azure.kusto.data import DataFormat, KustoConnectionStringBuilder
        from Hql.Data import Data
        import io
        import polars as pl

        kcsb_ingest = KustoConnectionStringBuilder.with_aad_application_key_authentication(
            self.cluster.replace("https://", "https://ingest-"), self.client_id, self.client_secret, self.tenant_id
        )

        ingest_client = QueuedIngestClient(kcsb_ingest)

        for i in ctx.data:
            if not isinstance(i.df, pl.DataFrame):
                logging.warning(f'{i.name} does not contain a dataframe, continuing...')
                continue

            self.ensure_table(i.name, i.df.schema)
            
            properties = IngestionProperties(
                database=self.database,
                table=i.name,
                data_format=DataFormat.CSV,
            )

            # Kusto SDK expects a file-like stream; serialize Polars to CSV in memory.
            buffer = io.BytesIO()
            i.df.write_csv(buffer)
            buffer.seek(0)

            ingest_client.ingest_from_stream(buffer, ingestion_properties=properties)

        return True 
