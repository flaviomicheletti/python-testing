import pytest
from abc import ABC, abstractmethod


class DataSource(ABC):
    # Abstract interface for a data source

    @abstractmethod
    def read_data(self):
        return "foo" # pragma: no cover


class FileDataSource(DataSource):
    # Concrete implementation of a file data source
    def read_data(self):
        # Code to read data from a file
        return "Reading data from a file"


class DatabaseDataSource(DataSource):
    # Concrete implementation of a database data source
    def read_data(self):
        # Code to read data from a database
        return "Reading data from a database"


class DataProcessor:
    # High-level module that depends on the DataSource interface
    def __init__(self, data_source):
        self.data_source = data_source

    def process_data(self):
        # Code to process the data
        data = self.data_source.read_data()
        return data


def test_process_data_file_data_source():
    # Create an instance of the FileDataSource
    file_data_source = FileDataSource()

    # Create an instance of the DataProcessor and pass in the FileDataSource instance
    data_processor = DataProcessor(file_data_source)

    # Use the DataProcessor to process the data
    result = data_processor.process_data()
    assert result == "Reading data from a file"

def test_process_data_data_basea_source():
    # Create an instance of the FileDataSource
    data_basea_source = DatabaseDataSource()

    # Create an instance of the DataProcessor and pass in the FileDataSource instance
    data_processor = DataProcessor(data_basea_source)

    # Use the DataProcessor to process the data
    result = data_processor.process_data()
    assert result == "Reading data from a database"



