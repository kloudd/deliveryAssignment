import math

def calculate_haversine(lon1, lat1, lon2, lat2):
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def split_string(string):
    return string.split(',')


def removeDEfromsortedDEs(assigned_executive, DEs):
    for de in DEs:
        if de.id == assigned_executive:
            DEs.remove(de)
    return DEs
