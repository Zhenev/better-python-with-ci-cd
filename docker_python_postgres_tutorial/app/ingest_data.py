import os
from dotenv import load_dotenv

import wget
from urllib.error import HTTPError

import sys
from time import time

import pandas as pd
from sqlalchemy import create_engine


load_dotenv('/app/python_connection.env')


def __fetch_downloaded_file_name(url_string):
    file_name = url_string.split('/')[-1]
    if url_string.endswith('.csv.gz') or url_string.endswith('.csv'):
        return file_name
    else:
        return ''


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

    print(user)
    print(url)

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

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

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
