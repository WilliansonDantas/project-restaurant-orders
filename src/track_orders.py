class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        newOrder = {
            "customer": customer,
            "order": order,
            "day": day
        }
        self.orders.append(newOrder)

    def get_most_ordered_dish_per_customer(self, customer):
        orderedDishPerCustomer = {}
        ordersList = self.orders

        for item in ordersList:
            if item['order'] in orderedDishPerCustomer:
                orderedDishPerCustomer[item['order']] += 1
            else:
                orderedDishPerCustomer[item['order']] = 1
        orderedFavorite = max(orderedDishPerCustomer,
                              key=lambda chave: orderedDishPerCustomer[chave])
        return orderedFavorite

    def get_never_ordered_per_customer(self, customer):
        allFoods = set()
        ordersFood = set()
        ordersList = self.orders

        for food in ordersList:
            allFoods.add(food['order'])

        for item in ordersList:
            if item['customer'] == customer:
                ordersFood.add(item['order'])

        neverOrders = allFoods - ordersFood
        return neverOrders

    def get_days_never_visited_per_customer(self, customer):
        allDays = set()
        ordersDays = set()
        ordersList = self.orders

        for day in ordersList:
            allDays.add(day['day'])

        for item in ordersList:
            if item['customer'] == customer:
                ordersDays.add(item['day'])

        daysNeverVisited = allDays - ordersDays
        return daysNeverVisited

    def get_busiest_day(self):
        busiestDay = {}
        ordersList = self.orders

        for item in ordersList:
            if item['day'] in busiestDay:
                busiestDay[item['day']] += 1
            else:
                busiestDay[item['day']] = 1
        busiestDayMax = max(busiestDay,
                            key=lambda chave: busiestDay[chave])
        return busiestDayMax

    def get_least_busy_day(self):
        pass
