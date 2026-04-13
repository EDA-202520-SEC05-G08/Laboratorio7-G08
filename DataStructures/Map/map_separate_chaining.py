import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_entry as me


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


def new_map(num_elements, load_factor, prime=109345121):
    capacity = next_prime(int(num_elements / load_factor))

    table = lt.new_list()
    for _ in range(capacity):
        bucket = lt.new_list()
        lt.add_last(table, bucket)

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
    
    
def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1    

def put(my_map, key, value):
    hv = hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hv)

    for i in range(lt.size(bucket)):
        entry = lt.get_element(bucket,i)
        if default_compare(key,entry) == 0:
            me.set_value(entry,value)
            return my_map
    
    new_entry = me.new_map_entry(key,value)
    lt.add_last(bucket,new_entry)
    my_map["size"] += 1

    my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map


def contains(my_map, key):
    hv = hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hv)
    for i in range(lt.size(bucket)):
        entry = lt.get_element(bucket,i)
        if default_compare(key,entry) == 0:
            return True
    return False


def get(my_map, key):
    hv = hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hv)

    for i in range(lt.size(bucket)):
        entry = lt.get_element(bucket,i)
        if default_compare(key,entry) == 0:
            return me.get_value(entry)
    return None


def remove(my_map, key):
    hv = hash_value(my_map, key)
    bucket = lt.get_element(my_map["table"], hv)

    for i in range(lt.size(bucket)):
        entry = lt.get_element(bucket,i)
        if default_compare(key,entry) == 0:
            lt.delete_element(bucket,i)
            my_map["size"] -= 1
            my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0