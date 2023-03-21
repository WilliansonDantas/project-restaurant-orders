import os


def maria(data):
    maria_orders_make = {}
    for item in data:
        if item[0] == 'maria' and item[1] in maria_orders_make:
            maria_orders_make[item[1]] += 1
        if item[0] == 'maria' and item[1] not in maria_orders_make:
            maria_orders_make[item[1]] = 1
    maria_food_favorite = max(maria_orders_make,
                              key=lambda chave: maria_orders_make[chave])
    return maria_food_favorite


def arnaldo(data):
    arnaldo_count = 0
    for item in data:
        if item[0] == 'arnaldo' and item[1] == 'hamburguer':
            arnaldo_count += 1
    return arnaldo_count


def joao_menu(data):
    joao_orders_food = set()
    menu = set()

    for item in data:
        menu.add(item[1])
        if item[0] == "joao":
            joao_orders_food.add(item[1])

    joao_never_order = menu - joao_orders_food
    return joao_never_order


def joao_days(data):
    joao_days = set()
    days = set()

    for item in data:
        days.add(item[2])
        if item[0] == "joao":
            joao_days.add(item[2])

    joao_day_never_visited = days - joao_days
    return joao_day_never_visited


def analyze_log(path_to_file):
    _, file_extension = os.path.splitext(path_to_file)
    if file_extension != '.csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'\n")
    try:
        with open(path_to_file, 'r') as file:
            data = []
            for line in file:
                data.append(line.strip().split(','))
        maria_func = maria(data)
        arnaldo_func = arnaldo(data)
        joao_menu_func = joao_menu(data)
        joao_days_func = joao_days(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(f"{maria_func}\n")
        f.write(f"{arnaldo_func}\n")
        f.write(f"{joao_menu_func}\n")
        f.write(f"{joao_days_func}\n")
