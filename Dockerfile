FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

COPY src ./src

COPY workspace.yml .

RUN pip install .

EXPOSE 3000

EXPOSE 4000