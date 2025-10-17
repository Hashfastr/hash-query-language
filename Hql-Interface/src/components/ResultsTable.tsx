import { useMemo, useState } from 'react';
import {
  useReactTable,
  getCoreRowModel,
  getSortedRowModel,
  getPaginationRowModel,
  getFilteredRowModel,
  flexRender,
  type ColumnDef,
  type SortingState,
} from '@tanstack/react-table';
import type { QueryResult } from '../types';

interface ResultsTableProps {
  results: QueryResult | null;
}

export function ResultsTable({ results }: ResultsTableProps) {
  const [sorting, setSorting] = useState<SortingState>([]);
  const [globalFilter, setGlobalFilter] = useState('');

  const columns = useMemo<ColumnDef<Record<string, any>>[]>(() => {
    if (!results || results.columns.length === 0) return [];

    return results.columns.map((col) => ({
      // Use accessor function instead of accessorKey to handle dot notation
      id: col,
      accessorFn: (row) => row[col],
      header: col,
      cell: (info) => {
        const value = info.getValue();
        if (value === null || value === undefined) {
          return <span className="text-gruvbox-light-gray dark:text-gruvbox-dark-gray">null</span>;
        }
        if (typeof value === 'object') {
          return <span className="text-gruvbox-light-purple dark:text-gruvbox-dark-purple">{JSON.stringify(value)}</span>;
        }
        return String(value);
      },
    }));
  }, [results]);

  const table = useReactTable({
    data: results?.data || [],
    columns,
    state: {
      sorting,
      globalFilter,
    },
    onSortingChange: setSorting,
    onGlobalFilterChange: setGlobalFilter,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    initialState: {
      pagination: {
        pageSize: 50,
      },
    },
  });

  if (!results) {
    return (
      <div className="flex items-center justify-center h-64 text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
        Execute a query to see results
      </div>
    );
  }

  if (results.data.length === 0) {
    return (
      <div className="p-4">
        <div className="card">
          <p className="text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
            Query executed successfully but returned no results.
          </p>
          {results.duration && (
            <p className="text-sm mt-2">Execution time: {results.duration.toFixed(3)}s</p>
          )}
        </div>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex items-center justify-between p-4 border-b border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
        <div className="flex items-center gap-4">
          <h3 className="font-bold">Results ({results.rowCount} rows)</h3>
          {results.duration && (
            <span className="text-sm text-gruvbox-light-gray dark:text-gruvbox-dark-gray">
              {results.duration.toFixed(3)}s
            </span>
          )}
        </div>
        <input
          type="text"
          value={globalFilter}
          onChange={(e) => setGlobalFilter(e.target.value)}
          placeholder="Filter results..."
          className="input w-64"
        />
      </div>

      <div className="flex-1 overflow-auto">
        <table className="w-full">
          <thead className="sticky top-0">
            {table.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <th
                    key={header.id}
                    className="table-header cursor-pointer select-none"
                    onClick={header.column.getToggleSortingHandler()}
                  >
                    <div className="flex items-center gap-1">
                      {flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                      {{
                        asc: ' ↑',
                        desc: ' ↓',
                      }[header.column.getIsSorted() as string] ?? null}
                    </div>
                  </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody>
            {table.getRowModel().rows.map((row) => (
              <tr
                key={row.id}
                className="hover:bg-gruvbox-light-bg1 dark:hover:bg-gruvbox-dark-bg1"
              >
                {row.getVisibleCells().map((cell) => (
                  <td key={cell.id} className="table-cell">
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex items-center justify-between p-4 border-t border-gruvbox-light-bg2 dark:border-gruvbox-dark-bg2">
        <div className="flex items-center gap-2">
          <button
            onClick={() => table.setPageIndex(0)}
            disabled={!table.getCanPreviousPage()}
            className="btn"
          >
            {'<<'}
          </button>
          <button
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
            className="btn"
          >
            {'<'}
          </button>
          <button
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
            className="btn"
          >
            {'>'}
          </button>
          <button
            onClick={() => table.setPageIndex(table.getPageCount() - 1)}
            disabled={!table.getCanNextPage()}
            className="btn"
          >
            {'>>'}
          </button>
        </div>
        <span className="text-sm">
          Page {table.getState().pagination.pageIndex + 1} of{' '}
          {table.getPageCount()}
        </span>
        <select
          value={table.getState().pagination.pageSize}
          onChange={(e) => table.setPageSize(Number(e.target.value))}
          className="input"
        >
          {[10, 25, 50, 100].map((pageSize) => (
            <option key={pageSize} value={pageSize}>
              Show {pageSize}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}
