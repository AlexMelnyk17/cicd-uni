import json
from population import parse_population_data, calculate_population_change

def main():

    file_path = input("Введіть шлях до файлу: ")
    print(f"--- 1. Зчитування даних з файлу '{file_path}' ---")
    data = parse_population_data(file_path)

    print("--- 2. Розрахунок динаміки населення ---")
    changes = calculate_population_change(data)

    print("Результат:")
    print(json.dumps(changes, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()