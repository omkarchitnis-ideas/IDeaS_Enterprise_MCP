# ==============================================================================
# SAS IDeaS Master Enterprise Unified Super-MCP Server Container
# Hosting 168 Canonical Tools across all 6 Core Enterprise Systems
# ==============================================================================
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (curl for healthcheck, build tools for native drivers)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies for all 6 enterprise domains
RUN pip install --no-cache-dir \
    fastapi>=0.110.0 \
    uvicorn>=0.30.0 \
    pydantic>=2.7.0 \
    python-dotenv>=1.0.1 \
    requests>=2.32.0 \
    starlette>=0.37.0 \
    pymssql>=2.3.0 \
    psycopg2-binary>=2.9.9 \
    qdrant-client \
    beautifulsoup4 \
    mcp

# Copy application files and domain modules
COPY sfdc_mcp_server.py /app/sfdc_mcp_server.py
COPY cma_mcp_server.py /app/cma_mcp_server.py
COPY optix_mcp_server.py /app/optix_mcp_server.py
COPY confluence_mcp_server.py /app/confluence_mcp_server.py
COPY datadog_mcp_server.py /app/datadog_mcp_server.py
COPY ups_mcp_server.py /app/ups_mcp_server.py
COPY unified_mcp_server.py /app/unified_mcp_server.py
COPY chains_cache.json /app/chains_cache.json
COPY data/g3_help_docs /app/data/g3_help_docs

# Expose Unified MCP HTTP SSE Port
EXPOSE 8550

# Container Healthcheck Probe
HEALTHCHECK --interval=15s --timeout=5s --start-period=15s --retries=3 \
    CMD curl -f http://localhost:8550/health || exit 1

# Start Unified Super-MCP Server
CMD ["python", "unified_mcp_server.py", "--host", "0.0.0.0", "--port", "8550"]
