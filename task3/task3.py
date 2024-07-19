import json
import sys

def setter(values_data, tests_data, report_path):
    results = {}
    values_array = values_data['values']

    for value_obj in values_array:
        value = value_obj
        results[value['id']] = value['value']

    with open(report_path, 'w') as file:
        json.dump(tests_data, file)  # копируем структуру tests в файл report.json

    with open(report_path, 'r') as file:
        report_data = json.load(file)

    # проставим значения "value: значение"
    report_data['tests'] = array_parser(report_data['tests'], results)

    # внесем изменения
    with open(report_path, 'w') as file:
        json.dump(report_data, file, indent=2)

def array_parser(values, results):
    for i, test in enumerate(values):
        if 'values' in test:
            test['values'] = array_parser(test['values'], results)

        if 'value' in test and 'id' in test and test['id'] in results:
            test['value'] = results[test['id']]

    return values

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python task3.py values.json tests.json report.json")
    else:
        values_path = sys.argv[1] # Получаем пути к файлам json
        tests_path = sys.argv[2]
        report_path = sys.argv[3]

data = {}
with open(values_path, 'r') as file:
    data['values'] = json.load(file)
with open(tests_path, 'r') as file:
    data['tests'] = json.load(file)

setter(data['values'], data['tests'], report_path)

print("Обновленные данные успешно сохранены в файл", report_path)
