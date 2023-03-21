import os
import sys


def analyze_log(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)
    if file_extension != '.csv':
        return sys.stderr.write(f"Extensão inválida: '{path_to_file}'\n")
    try:
        with open(path_to_file, 'r') as file:
            data = []
            lines = file.readlines()
            for line in lines:
                data.append(line.strip().split(','))
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo inexistente: '{path_to_file}'")
    
    maria_orders_make = {}
    arnaldo_count = 0
    joao_orders_food = set()
    joao_days = set()
    menu = set()
    days = set()

    for item in data:
        menu.add(item[1])
        days.add(item[2])
        if item[0] == 'maria' and item[1] in maria_orders_make:
            maria_orders_make[item[1]] += 1
        if item[0] == 'maria' and item[1] not in maria_orders_make:
            maria_orders_make[item[1]] = 1
        if item[0] == 'arnaldo' and item[1] == 'hamburguer':
            arnaldo_count += 1
        if item[0] == "joao":
            joao_orders_food.add(item[1])
            joao_days.add(item[2])

    maria_food_favorite = max(maria_orders_make, key=lambda chave: maria_orders_make[chave])

    joao_never_order = menu - joao_orders_food
    joao_never_order_sorted = ', '.join(sorted(joao_never_order))

    joao_day_never_visited = days - joao_days
    joao_day_never_visited_sorted = ', '.join(sorted(joao_day_never_visited))

    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(f"{maria_food_favorite}\n")
        f.write(f"{arnaldo_count}\n")
        f.write(f"{joao_never_order_sorted}\n")
        f.write(f"{joao_day_never_visited_sorted}\n")