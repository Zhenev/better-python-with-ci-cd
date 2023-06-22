import unittest
from docker_python_postgres_tutorial.app.ingest_data import fetch_downloaded_file_name


class TestIngestData(unittest.TestCase):

    def test_fetch_downloaded_file_name(self):
        tests = [
            {'input_url': 'abc.csv', 'output': 'abc.csv'},
            {'input_url': 'abc.csv.gz', 'output': 'abc.csv.gz'},
            {'input_url': 'abc/', 'output': ''}
        ]
        for test in tests:
            assert fetch_downloaded_file_name(test['input_url']) == test['output']


if __name__ == '__main__':
    unittest.main()
