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
def test_parse_population_data(sample_data_file):
    data = parse_population_data(sample_data_file)
    assert len(data) == 4

    assert data[0] == {'country': 'Ukraine', 'year': 2020, 'population': 41000000}
    assert data[3] == {'country': 'Poland', 'year': 2021, 'population': 37900000}



@pytest.mark.parametrize("input_data, expected_result", [
    (
        [
            {'country': 'CountryA', 'year': 2000, 'population': 1000},
            {'country': 'CountryA', 'year': 2001, 'population': 1020},
        ],
        {'CountryA': {'2000→2001': 20}},
    ),
    (
        [
            {'country': 'CountryB', 'year': 2011, 'population': 500},
            {'country': 'CountryB', 'year': 2010, 'population': 400},
        ],
        {'CountryB': {'2010→2011': 100}},
    ),
    (
        [
            {'country': 'CountryC', 'year': 2020, 'population': 1000},
            {'country': 'CountryC', 'year': 2021, 'population': 950},
        ],
        {'CountryC': {'2020→2021': -50}},
    ),
    (
        [
            {'country': 'CountryD', 'year': 2020, 'population': 5000},
        ],
        {'CountryD': {}},
    ),
    (
        [
            {'country': 'Ukraine', 'year': 2000, 'population': 48000000},
            {'country': 'Ukraine', 'year': 2001, 'population': 47500000},
            {'country': 'Poland',  'year': 2000, 'population': 38000000},
            {'country': 'Poland',  'year': 2001, 'population': 38100000},
        ],
        {
            'Ukraine': {'2000→2001': -500000},
            'Poland':  {'2000→2001':  100000},
        },
    ),
])
def test_calculate_population_change(input_data, expected_result):
    assert calculate_population_change(input_data) == expected_result