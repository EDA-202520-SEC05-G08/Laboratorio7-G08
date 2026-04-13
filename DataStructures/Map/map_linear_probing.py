import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me

EMPTY = "__EMPTY__"

# Funciones auxiliares

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

def hash_value(my_map, key):
    return ((my_map["scale"] * hash(key) + my_map["shift"]) % my_map["prime"]) % my_map["capacity"]

def is_available(table, pos):
    entry = lt.get_element(table, pos)
    return me.get_key(entry) is None or me.get_key(entry) == EMPTY

def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def find_slot(my_map, key, hv):
    first_avail = None

    while True:
        entry = lt.get_element(my_map["table"], hv)

        if is_available(my_map["table"], hv):
            if first_avail is None:
                first_avail = hv
            if me.get_key(entry) is None:
                return False, first_avail

        elif default_compare(key, entry) == 0:
            return True, hv

        hv = (hv + 1) % my_map["capacity"]
        
#funciones pedidas     
   
def new_map(num_elements, load_factor, prime=109345121):
    capacity = next_prime(int(num_elements / load_factor))

    table = lt.new_list()
    for _ in range(capacity):
        lt.add_last(table, me.new_map_entry(None, None))

    return {
        "prime": prime,
        "capacity": capacity,
        "scale": 1,   
        "shift": 0,   
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }


def put(my_map, key, value):
    hv = hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hv)

    entry = lt.get_element(my_map["table"], pos)

    if found:
        me.set_value(entry, value)
    else:
        lt.change_info(my_map["table"], pos, me.new_map_entry(key, value))
        my_map["size"] += 1

    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map


def contains(my_map, key):
    hv = hash_value(my_map, key)
    found, _ = find_slot(my_map, key, hv)
    return found


def get(my_map, key):
    hv = hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hv)

    if found:
        entry = lt.get_element(my_map["table"], pos)
        return me.get_value(entry)
    return None


def remove(my_map, key):
    hv = hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hv)

    if found:
        lt.change_info(my_map["table"], pos, me.new_map_entry(EMPTY, EMPTY))
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map


def size(my_map):
    return my_map["size"]

def rehash(my_map):

    old_table = my_map["table"]
    old_capacity = my_map["capacity"]

    # Nueva capacidad = siguiente primo del doble
    new_capacity = next_prime(2 * old_capacity)

    # Crear nueva tabla
    new_map_lp = new_map(new_capacity, my_map["limit_factor"], my_map["prime"])

    # Reiniciar correctamente
    new_map_lp["capacity"] = new_capacity

    # Reinsertar elementos
    for i in range(old_capacity):
        entry = lt.get_element(old_table, i)
        key = me.get_key(entry)
        value = me.get_value(entry)

        if key is not None and key != "__EMPTY__":
            put(new_map_lp, key, value)

    return new_map_lp

def is_empty(my_map):
    return my_map["size"] == 0