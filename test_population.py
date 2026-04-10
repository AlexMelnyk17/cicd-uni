import pytest
import os
import tempfile
from population import parse_population_data, calculate_population_change

@pytest.fixture
def sample_data_file():
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write("Ukraine, 2020, 41000000\n")
        f.write("Ukraine, 2021, 40000000\n")
        f.write("Poland, 2020, 38000000\n")
        f.write("Poland, 2021, 37900000\n")
        f.write("InvalidCountry, 2022\n")   
    yield path
    os.remove(path)

