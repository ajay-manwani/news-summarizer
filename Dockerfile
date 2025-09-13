FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install uv
RUN pip install --no-cache-dir uv

# Copy pyproject + lockfile first for caching
COPY pyproject.toml uv.lock ./

# Install deps into system environment
RUN uv sync --frozen --no-cache --no-dev --system

# Copy the rest of the app
COPY . .

CMD ["uv", "run", "python", "main.py"]