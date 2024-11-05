FROM python:3.12.1-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock* ./

COPY . /usr/src/app

RUN poetry install

# Run the command (modify here)
CMD ["sh", "-c", "cd /usr/src/app && poetry run python ./example_problem/main.py"]
