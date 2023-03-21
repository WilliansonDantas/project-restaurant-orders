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
                return data.append(line.strip().split(','))
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo inexistente: '{path_to_file}'")
    
    print(data)
    maria_orders_make = {}
    arnaldo_count = 0
    joao_orders_food = set()
    joao_days = set()

    customers = set()
    snacks = set()
    allDays = set()

    for item in data:
        customers.add(item[0])
        snacks.add(item[1])
        allDays.add(item[2])

    for customer in customers:
        if customer == 'maria':
            for snack in snacks:
                if snack in maria_orders_make:
                    maria_orders_make[snack] += 1
                else:
                    maria_orders_make[snack] = 1
                
    for customer in customers:
        if customer == 'arnaldo':
            for snack in snacks:
                if snack == 'hamburguer':
                    arnaldo_count += 1

    for customer in customers:
        if customer == 'joao':
            joao_orders_food.add(item[1])
    for dayD in allDays:
            joao_days.add(dayD)

    # print(maria_orders_make)
    maria_food_favorite = max(maria_orders_make, key=lambda chave: maria_orders_make[chave])

    menu = set()
    for order in snacks:
        menu.add(order[1])
    joao_never_order = menu - joao_orders_food
    # print(joao_never_order)
    joao_never_order_sorted = ', '.join(sorted(joao_never_order))

    day = set()
    for order in snacks:
        day.add(order[2])
    joao_day_never_visited = day - joao_days
    # print(joao_day_never_visited)
    joao_day_never_visited_sorted = ', '.join(sorted(joao_day_never_visited))

    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(f"{maria_food_favorite}\n")
        f.write(f"{arnaldo_count}\n")
        f.write(f"{joao_never_order_sorted}\n")
        f.write(f"{joao_day_never_visited_sorted}\n")