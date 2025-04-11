# syntax = docker/dockerfile:1.5
FROM python:3.12-bookworm
ENV PYTHONUNBUFFERED=1
# tell uv to use a python environment outside the code directory
ENV UV_PROJECT_ENVIRONMENT=/usr/local/venv/

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]