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