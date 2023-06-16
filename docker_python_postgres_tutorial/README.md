## Docker Python Postgres Tutorial

Welcome to the Building Data Pipelines with Docker Tutorial project repository!

The [tutorial](https://zhenev.github.io/2023-04-29-building-data-pipelines-with-docker/) provides a step-by-step guide on setting up a data ingestion pipeline using Docker, Python, and Postgres.

### Project Structure

- `app`: Contains the Python script for data ingestion and the Dockerfile for building the app container.
- `database`: The folder to store the persistent data for the Postgres database.
- `config`: Local folder, holds configuration files, such as environment variable files, for the project.

## Prerequisites

Before getting started, ensure that you have Docker Engine and Docker Compose installed:
- Visit the official Docker website and follow the installation instructions for your operating system.

### Usage
1. Clone the project repository to your local machine.
2. Update the configuration files in the `/config` directory with the appropriate values (see `/config/README.md`).
3. Check whether the ingestion script in the `/app` directory should be customized (depending on the data source file).
4. Run the application using the `docker-compose up` command.
5. Access the result, e.g. by using the `sqlalchemy` module:

```python
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(f'postgresql://{user}:{password}@:5431/{db}')
pd.read_sql(f"""SELECT * FROM {table_name} LIMIT 10""", con=engine)
```

### Support and Contributions

If you encounter any issues or have questions related to this tutorial or the project, please open an issue
in this repository. Contributions, suggestions, and feedback are also welcome!

### Resources

- Check the project blog post for detailed instructions and explanations.
- Visit the Docker and Postgres documentation for more information on Docker and Postgres.

