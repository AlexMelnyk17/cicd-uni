from collections import defaultdict

def parse_population_data(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 3:
                country = parts[0].strip()
                year = int(parts[1].strip())
                population = int(parts[2].strip())
                data.append({'country': country, 'year': year, 'population': population})
    return data



def calculate_population_change(data: list[dict]) -> dict[str, dict]:
    country_data = defaultdict(list)

    for row in data:
        country_data[row['country']].append((row['year'], row['population']))

    changes = {}
    for country, records in country_data.items():
        records.sort(key=lambda x: x[0])
        country_changes = {}
        for i in range(1, len(records)):
            prev_year, prev_pop = records[i - 1]
            curr_year, curr_pop = records[i]
            country_changes[f"{prev_year}→{curr_year}"] = curr_pop - prev_pop
        changes[country] = country_changes

    return changes
