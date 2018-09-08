from utility_functions import split_string, calculate_haversine, removeDEfromsortedDEs


rules =  [['rule1', 'order_delay_time', orders],
          [],
          ['rule5', de, orders]
          ]


def order_delay_time(orders):
    return sorted(orders, key=lambda i: i.ordered_time, reverse=True)


def de_waiting_time(DEs):
    return sorted(DEs, key=lambda i: i.last_order_delivered_time, reverse=True)


def first_mile(order, DEs):
    lowest_first_mile = 10000
    assigned_executive = None

    order_lat_long = split_string(order.restaurant_location)
    for de in DEs:
        if de is not None:
            de_lat_long = split_string(de.current_location)
            result = calculate_haversine(int(order_lat_long[0]), int(order_lat_long[1]), int(de_lat_long[0]), int(de_lat_long[1]))
            if result < lowest_first_mile:
                lowest_first_mile = result
                assigned_executive = de.id
    return assigned_executive