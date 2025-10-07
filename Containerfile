FROM python:3.13-slim
WORKDIR /opt/Hql

COPY . .
RUN pip install --no-cache-dir .

ENTRYPOINT ["python3", "-m", "Hql"]
