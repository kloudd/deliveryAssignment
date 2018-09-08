import math
from priority_rules import rules

from priority_rules import first_mile,de_waiting_time,order_delay_time
from utility_functions import removeDEfromsortedDEs,calculate_haversine,split_string


def assignments(orders, DEs):
    # Implementing order delay time


    sorted_orders = order_delay_time(orders)


    sorted_DEs = de_waiting_time(DEs)

    assigned_orders = []
    for order in sorted_orders:

        assigned_executive = first_mile(order, sorted_DEs)
        new_dir = {}
        new_dir['order_id'] = order.id
        new_dir['de_id'] = assigned_executive
        assigned_orders.append(new_dir)

        sorted_DEs = removeDEfromsortedDEs(assigned_executive, sorted_DEs)
    display(assigned_orders)


def display(assigned_orders):
    for assigned_order in assigned_orders:
        print(assigned_order['order_id'], assigned_order['de_id'])



