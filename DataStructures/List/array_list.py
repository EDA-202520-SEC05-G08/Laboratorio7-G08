def new_list():
    newlist = {
        'elements':[], 'size':0,
        }
    return newlist

def get_element(my_list, index):
    return my_list['elements'][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size (my_list)->int:
    my_list["size"] = len(my_list['elements'])
    return my_list["size"]

def add_first (my_list, elemento):
    my_list = my_list["elements"].insert(0,elemento)
    return my_list

def add_last (my_list, elemento):
    my_list = my_list["elements"].append(elemento)

def first_element (my_list):
    elemento = my_list["elements"][0]
    return elemento 

def is_empty (my_list)-> bool:
    if size(my_list) == 0:
        return True
    else:
        return False

def last_element (my_list):
    elemento = my_list['elements'][-1]
    return elemento

def delete_element (my_list, posicion)-> list:
    if posicion < 0 or posicion >= my_list["size"]:
        return my_list

    my_list["elements"].pop(posicion)
    my_list["size"] -= 1
    return my_list
 
def remove_first (my_list)-> list:
    my_list = my_list['elements'].pop(0)
    return my_list    

def remove_last (my_list)-> list:
    my_list = my_list['elements'].pop(-1)
    return my_list 

def insert_element (my_list,elemento,posicion)->list:
    if posicion < 0 or posicion > my_list["size"]:
        return my_list

    my_list["elements"].insert(posicion, elemento)
    my_list["size"] += 1
    return my_list

def change_info (my_list,posicion,new_info)->list:
    my_list['elements'][posicion] = new_info
    return my_list

def exchange (my_list,pos_1,pos_2)->list:
    element_1 = my_list['elements'][pos_1]
    my_list['elements'][pos_1] = my_list['elements'][pos_2]
    my_list['elements'][pos_2] = element_1
    return my_list

def sub_list (my_list,pos_i,num_elements)->list:
    if pos_i < 0 or pos_i >= my_list["size"]:
        return None
    sub_elements = my_list["elements"][pos_i:pos_i + num_elements]
    new_sub_list = {
        "elements": sub_elements.copy(),
        "size": len(sub_elements)
    }

    return new_sub_list   

def price_sort_criteria(element_1, element_2):
    """
    Compara dos elementos.
    Retorna True si element_1 < element_2,
    False en caso contrario.
    """
    is_sorted = False

    if element_1["price"] > element_2["price"]:
        is_sorted = True
    elif element_1["price"] == element_2["price"]:
        if element_1["model"] < element_2["model"]:
            is_sorted = True
        else:
            is_sorted = False

    return is_sorted


def price_sort_weight_criteria(element_1, element_2):
    """
    Compara dos elementos.
    Retorna True si element_1 < element_2,
    False en caso contrario.
    """
    is_sorted = False

    if element_1["price"] > element_2["price"]:
        is_sorted = True
    elif element_1["price"] == element_2["price"]:
        if element_1["weight_kg"] > element_2["weight_kg"]:
            is_sorted = True
        else:
            is_sorted = False

    return is_sorted

def price_sort_weight_criteria_asc(element_1, element_2):
    """
    Compara dos elementos.
    Retorna True si element_1 < element_2,
    False en caso contrario.
    """
    is_sorted = False

    if element_1["price"] > element_2["price"]:
        is_sorted = True
    elif element_1["price"] == element_2["price"]:
        if element_1["weight_kg"] < element_2["weight_kg"]:
            is_sorted = True
        else:
            is_sorted = False

    return is_sorted

def efficient_sort_criteria(element_1, element_2):
    """
    Compara dos elementos.
    Retorna True si element_1 < element_2,
    False en caso contrario.
    """
    is_sorted = False
    
    
    if element_1["efficiency_score"] > element_2["efficiency_score"]:
        is_sorted = True
    elif element_1["efficiency_score"] == element_2["efficiency_score"]:
        if element_1["price"] < element_2["price"]:
            is_sorted = True
        else:
            is_sorted = False

    return is_sorted

def selection_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo Selection Sort.
    
    Parametros:
        my_list (array_list): Lista a ordenar.
        sort_crit (function): Función de comparación.
        
    Retorna:
        array_list: Lista ordenada.
    """

    size = my_list["size"]
    elements = my_list["elements"]

    for i in range(size):

        min_index = i

        for j in range(i + 1, size):

            if sort_crit(elements[j], elements[min_index]):
                min_index = j

        if min_index != i:
            elements[i], elements[min_index] = elements[min_index], elements[i]

    return my_list

def insertion_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo Insertion Sort.

    Parametros:
        my_list (array_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Retorna:
        array_list: Lista ordenada.
    """

    size = my_list["size"]
    elements = my_list["elements"]

    for i in range(1, size):

        current = elements[i]
        j = i - 1

        while j >= 0 and sort_crit(current, elements[j]):
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = current

    return my_list

def shell_sort(my_list, sort_crit):
    """
    Ordena una lista utilizando el algoritmo Shell Sort.

    Parametros:
        my_list (array_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Retorna:
        array_list: Lista ordenada.
    """

    size = my_list["size"]
    elements = my_list["elements"]

    if size <= 1:
        return my_list

    gap = size // 2

    while gap > 0:

        for i in range(gap, size):

            current = elements[i]
            j = i

            while j >= gap and sort_crit(current, elements[j - gap]):
                elements[j] = elements[j - gap]
                j -= gap

            elements[j] = current

        gap //= 2

    return my_list

def merge_sort(my_list, sort_crit):

    if my_list["size"] <= 1:
        return my_list

    mid = my_list["size"] // 2

    left = {
        "elements": my_list["elements"][:mid],
        "size": mid
    }

    right = {
        "elements": my_list["elements"][mid:],
        "size": my_list["size"] - mid
    }

    left = merge_sort(left, sort_crit)
    right = merge_sort(right, sort_crit)

    return merge(left, right, sort_crit)


def merge(left, right, sort_crit):

    result = {
        "elements": [],
        "size": 0
    }

    i = 0
    j = 0

    while i < left["size"] and j < right["size"]:

        if sort_crit(left["elements"][i], right["elements"][j]):
            result["elements"].append(left["elements"][i])
            i += 1
        else:
            result["elements"].append(right["elements"][j])
            j += 1

    while i < left["size"]:
        result["elements"].append(left["elements"][i])
        i += 1

    while j < right["size"]:
        result["elements"].append(right["elements"][j])
        j += 1

    result["size"] = len(result["elements"])

    return result

def quick_sort(my_list, sort_crit):

    if my_list["size"] <= 1:
        return my_list

    pivot = my_list["elements"][0]

    left = {"elements": [], "size": 0}
    equal = {"elements": [], "size": 0}
    right = {"elements": [], "size": 0}

    for element in my_list["elements"]:

        if sort_crit(element, pivot):
            left["elements"].append(element)

        elif sort_crit(pivot, element):
            right["elements"].append(element)

        else:
            equal["elements"].append(element)

    left["size"] = len(left["elements"])
    equal["size"] = len(equal["elements"])
    right["size"] = len(right["elements"])

    left = quick_sort(left, sort_crit)
    right = quick_sort(right, sort_crit)

    result = {
        "elements": left["elements"] + equal["elements"] + right["elements"],
        "size": left["size"] + equal["size"] + right["size"]
    }

    return result