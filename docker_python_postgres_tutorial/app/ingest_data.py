import os
from dotenv import load_dotenv

import wget
from urllib.error import HTTPError

import sys
from time import time, sleep

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


load_dotenv('/app/python_connection.env')


def fetch_downloaded_file_name(file_url: str) -> str:
    file_name = file_url.split('/')[-1]
    if file_url.endswith('.csv.gz') or file_url.endswith('.csv'):
        return file_name
    else:
        return ''


def check_database_health(db_url: str) -> bool:
    try:
        # Create an engine using the database URL
        engine = create_engine(db_url)

        # Try to connect to the database
        with engine.connect():
            return True  # Database connection successful

    except OperationalError:
        return False  # Database connection failed


def main():
    """The script takes a set of Postgres database connection parameters, table name, and url, reads a csv file,
    and uploads it into a Postgres db table. During the upload it reports how much time it took to upload each chunk
    and how many chunks have been uploaded.
    """
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    table_name = os.getenv("POSTGRES_TABLENAME")
    url = os.getenv("DATA_URL")

    # the backup files can be gzipped, keep the correct extension for pandas to be able to open the file
    csv_name = __fetch_downloaded_file_name(url)
    if csv_name:
        try:
            wget.download(url)
            print(f'\n{csv_name} downloaded.')
        except HTTPError:
            sys.exit(f'HTTP error, file not found at {url}')

    else:
        sys.exit(f'Unknown file format at {url}')

    database_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'

    # Wait for the database to become available
    while not check_database_health(database_url):
        print("Waiting for the database to become available...")
        sleep(10)  # Wait for 10 second before retrying

    engine = create_engine(database_url)

    pd.read_csv(csv_name).head(n=0).to_sql(name=table_name, con=engine, index=False, if_exists='replace')
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=50000)

    i = 1
    while True:

        try:
            t_start = time()

            df = next(df_iter)

            df.to_sql(name=table_name, con=engine, index=False, if_exists='append')

            t_end = time()

            print(f'inserted chunk {i}, took {(t_end - t_start):.3f} second')
            i += 1

        except StopIteration:
            print(f"Finished ingesting data into the postgres database, total num of chunks = {i - 1}")
            break


if __name__ == '__main__':
    main()
