FROM python:3.13-slim
WORKDIR /opt/Hql

# RUN apt-get update && apt-get install -y --no-install-recommends \
#         build-essential \
#         curl \
#         ca-certificates \
#         git \
#     && curl https://sh.rustup.rs -sSf | sh -s -- -y \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

# ENV PATH="/root/.cargo/bin:${PATH}"

COPY . .
RUN pip install --no-cache-dir .

ENTRYPOINT ["python3", "-m", "Hql"]
