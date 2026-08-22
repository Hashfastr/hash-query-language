###############
## Builder   ##
###############
FROM python:3.14-slim AS builder

ARG HOME="/opt/Hql"

# Build deps for polars / native wheels and frontend
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gcc \
        build-essential \
        rustup \
    && rm -rf /var/lib/apt/lists/*

RUN rustup default stable

# uv from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/
ENV PATH=/root/.cargo/bin:$PATH
# Copy mode keeps the venv self-contained (no hardlinks back into the cache).
ENV UV_LINK_MODE=copy

# python:3.14-slim ships GIL 3.14; .python-version pins to 3.14t.
RUN uv python install 3.14t

# Node.js for the frontend
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p $HOME
COPY ./Hql $HOME/Hql
COPY ./pyproject.toml $HOME
COPY ./.python-version $HOME
COPY ./LICENSE $HOME
COPY ./README.md $HOME
WORKDIR $HOME

# reduces file size greatly
ENV PYO3_USE_ABI3_FORWARD_COMPATIBILITY=0
ENV CARGO_PROFILE_RELEASE_STRIP=debuginfo

# --no-editable so pyhql lands as real files in site-packages and the runtime
# stage doesn't need /opt/Hql/Hql copied in just to satisfy a .pth pointer.
RUN uv sync --no-dev --no-editable

COPY ./Hql-Interface $HOME/Hql-Interface
WORKDIR $HOME/Hql-Interface
RUN npm install && npm run build

###############
## Runtime   ##
###############
FROM python:3.14-slim

# Bring across the venv, the managed 3.14t interpreter the venv symlinks into,
# and the built frontend (served from a hardcoded path by Hql/Apiserver).
COPY --from=builder /opt/Hql/.venv /opt/Hql/.venv
COPY --from=builder /opt/Hql/.local /opt/Hql/.local
COPY --from=builder /opt/Hql/Hql-Interface/dist /opt/Hql/Hql-Interface/dist

ARG USER="root"
ARG HOME="/data"

RUN mkdir -p "$HOME" && \
    chown -R "$USER:$USER" "$HOME"
USER "$USER"
WORKDIR "$HOME"

ENV PYTHON_GIL=0
ENTRYPOINT ["/opt/Hql/.venv/bin/python", "-m", "Hql"]
