## Configuration Files

This folder should contain configuration files used in the Docker Python Postgres Tutorial project.
These files are essential for configuring the environment and parameters of the application.

### File Descriptions

- `python_connection.env`: This file contains the connection arguments and configuration parameters for the
`ingest_data.py` script:
  - POSTGRES_USER=your_user
  - POSTGRES_PASSWORD=your_password 
  - POSTGRES_DB=your_db_name
  - POSTGRES_HOST=your_db_hostname # the same as the database service name in the `compose.yml` file 
  - POSTGRES_PORT=5432
  - POSTGRES_TABLENAME=your_table_name 
  - DATA_URL=https://your/url.csv
- `postgres_db.env`: This file contains the configuration parameters for the Postgres database to be set up:
  - POSTGRES_USER=your_user
  - POSTGRES_PASSWORD=your_password 
  - POSTGRES_DB=your_db_name

### Usage

1. Update the `.env` files with the appropriate values for your environment and application setup.
2. The `.env` files are mounted for corresponding services in the Docker `compose.yml` file to ensure that the
configuration files are accessible within the container during runtime.

### Important Note

Please ensure that sensitive information, such as credentials or private keys, is not committed to version control.
Use appropriate security measures, such as proper file permissions or encryption, to protect sensitive data.

### Support and Contributions

If you have any questions related to the project, please reach out by opening an issue in the project repository.
Contributions, suggestions, and feedback are also welcome!

