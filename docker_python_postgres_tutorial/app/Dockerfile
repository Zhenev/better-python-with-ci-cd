FROM python:3.10

RUN pip3 install poetry==1.2.2

WORKDIR /app
COPY ./pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-root --without dev

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
COPY ./app/ingest_data.py .


ENTRYPOINT ["poetry", "run", "python", "ingest_data.py"]

