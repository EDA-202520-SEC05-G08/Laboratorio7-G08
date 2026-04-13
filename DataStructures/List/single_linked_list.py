def new_list():
    newlist = {
        'first':None, 
        'last':None,
        'size':0,
        }
    return newlist

def get_element(my_list, pos):
    searchpos=0
    node = my_list["first"]
    while searchpos < pos:
        node=node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
        
    if not is_in_array:
        count = -1
    return count

def size (my_list):
    return my_list["size"]

def add_first (my_list, elemento):
    new_node = {
        "info": elemento,
        "next": my_list["first"]
    }
    my_list["first"] = new_node
    if my_list["size"] == 0:
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def add_last (my_list, elemento):
    new_node = {
        "info": elemento,
        "next": None
    }
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def first_element (my_list):
    return my_list["first"]["info"]
    
def is_empty(my_list) -> bool:
    if my_list["first"] is None:
        return True
    else:
        return False

def last_element(my_list):
    if my_list["size"] == 0:
        return None
    else:
        return my_list["last"]["info"]
    
def delete_element(my_list, posicion) -> list:
    if my_list["size"] == 0:
        return my_list

    if posicion == 0:
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        if my_list["size"] == 0:
            my_list["last"] = None
        return my_list

    prev = my_list["first"]
    index = 0

    while index < posicion - 1 and prev["next"] is not None:
        prev = prev["next"]
        index += 1

    nodo_eliminar = prev["next"]
    if nodo_eliminar is not None:
        prev["next"] = nodo_eliminar["next"]

        if nodo_eliminar == my_list["last"]:
            my_list["last"] = prev

        my_list["size"] -= 1

    return my_list
 
def remove_first (my_list):
    if my_list["size"] == 0:
        return None
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return removed     

def remove_last(my_list):
    if my_list["size"] == 0:
        return None

    if my_list["size"] == 1:
        removed = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        return removed

    current = my_list["first"]

    while current["next"] != my_list["last"]:
        current = current["next"]

    removed = my_list["last"]["info"]
    current["next"] = None
    my_list["last"] = current
    my_list["size"] -= 1

    return removed

def insert_element(my_list, elemento, posicion) -> list:
    if posicion < 0 or posicion > my_list["size"]:
        return my_list

    if posicion == 0:
        return add_first(my_list, elemento)

    if posicion == my_list["size"]:
        return add_last(my_list, elemento)

    new_node = {
        "info": elemento,
        "next": None
    }

    prev = my_list["first"]
    index = 0

    while index < posicion - 1:
        prev = prev["next"]
        index += 1

    new_node["next"] = prev["next"]
    prev["next"] = new_node

    my_list["size"] += 1
    return my_list

def change_info (my_list,posicion,new_info)->list:
    valor_base = my_list["first"]
    count = 0
    while count < posicion:
        valor_base = valor_base["next"]
        count += 1

    valor_base["info"] = new_info
    return my_list

def exchange (my_list,posicion1,posicion2)->list:
    
    if posicion1 == posicion2:
        return my_list

    valor_base1 = my_list["first"]
    contador = 0
    
    while contador < posicion1:
        valor_base1 = valor_base1["next"]
        contador += 1

    valor_base2 = my_list["first"]
    contador = 0
    
    while contador < posicion2:
        valor_base2 = valor_base2["next"]
        contador += 1

    valor_guardado = valor_base1["info"]
    valor_base1["info"] = valor_base2["info"]
    valor_base2["info"] = valor_guardado

    return my_list

def sub_list (my_list,posicion_inicial, cantidad)->list:
    
    nueva_lista = new_list()

    if my_list["first"] is None:
        return nueva_lista

    actual = my_list["first"]
    contador = 0

    while contador < posicion_inicial:
        actual = actual["next"]
        contador += 1

    copiados = 0

    while actual is not None and copiados < cantidad:
        nuevo = {"info": actual["info"], "next": None}

        if nueva_lista["first"] is None:
            nueva_lista["first"] = nuevo
            nueva_lista["last"] = nuevo
        else:
            nueva_lista["last"]["next"] = nuevo
            nueva_lista["last"] = nuevo

        nueva_lista["size"] += 1
        actual = actual["next"]
        copiados += 1

    return nueva_lista 

def default_sort_criteria(element_1, element_2):
    """
    Función de comparación por defecto.

    Parametros:
        element_1 (any): Primer elemento a comparar.
        element_2 (any): Segundo elemento a comparar.

    Retorna:
        bool: True si element_1 < element_2,
              False en caso contrario.
    """

    if element_1["title"] < element_2["title"]:
        return True
    else:
        return False

def selection_sort(my_list, sort_crit):
    """
    Ordena una single linked list utilizando el algoritmo Selection Sort.

    Parametros:
        my_list (single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Retorna:
        single_linked_list: Lista ordenada.
    """

    if my_list["size"] <= 1:
        return my_list

    current = my_list["first"]

    while current is not None:

        min_node = current
        search = current["next"]

        while search is not None:
            if sort_crit(search["info"], min_node["info"]):
                min_node = search
            search = search["next"]

        temp = current["info"]
        current["info"] = min_node["info"]
        min_node["info"] = temp

        current = current["next"]

    return my_list

def insertion_sort(my_list, sort_crit):
    """
    Ordena una single linked list utilizando el algoritmo Insertion Sort.

    Parametros:
        my_list (single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Retorna:
        single_linked_list: Lista ordenada.
    """

    if my_list["size"] <= 1:
        return my_list

    sorted_head = None
    current = my_list["first"]

    while current is not None:

        next_node = current["next"]

        if sorted_head is None or sort_crit(current["info"], sorted_head["info"]):
            current["next"] = sorted_head
            sorted_head = current
        else:
            search = sorted_head

            while (search["next"] is not None and
                   not sort_crit(current["info"], search["next"]["info"])):
                search = search["next"]

            current["next"] = search["next"]
            search["next"] = current

        current = next_node

    my_list["first"] = sorted_head
    return my_list

def shell_sort(my_list, sort_crit):
    """
    Ordena una single linked list utilizando el algoritmo Shell Sort.

    Parametros:
        my_list (single_linked_list): Lista a ordenar.
        sort_crit (function): Función de comparación.

    Retorna:
        single_linked_list: Lista ordenada.
    """

    size = my_list["size"]

    if size <= 1:
        return my_list

    elements = []
    current = my_list["first"]

    while current is not None:
        elements.append(current["info"])
        current = current["next"]

    gap = size // 2

    while gap > 0:
        for i in range(gap, size):

            temp = elements[i]
            j = i

            while j >= gap and sort_crit(temp, elements[j - gap]):
                elements[j] = elements[j - gap]
                j -= gap

            elements[j] = temp

        gap //= 2

    current = my_list["first"]
    index = 0

    while current is not None:
        current["info"] = elements[index]
        current = current["next"]
        index += 1

    return my_list

def merge_sort(my_list, sort_crit):
    """
    Ordena una lista enlazada simple utilizando el algoritmo Merge Sort.

    :param my_list: single_linked_list
    :param sort_crit: función de comparación
    :return: lista ordenada
    """

    if my_list is None:
        return my_list

    if my_list["first"] is None:
        return my_list

    if my_list["first"]["next"] is None:
        return my_list

    left, right = _split(my_list)

    left = merge_sort(left, sort_crit)
    right = merge_sort(right, sort_crit)

    return _merge(left, right, sort_crit)

#funcion auxiliar
def _split(my_list):

    left = new_list()
    right = new_list()

    if my_list["first"] is None or my_list["first"]["next"] is None:
        return my_list, right

    slow = my_list["first"]
    fast = my_list["first"]["next"]

    while fast is not None and fast["next"] is not None:
        slow = slow["next"]
        fast = fast["next"]["next"]

    middle = slow["next"]
    slow["next"] = None  # Cortamos la lista

    current = my_list["first"]
    while current is not None:
        left = add_last(left, current["info"])
        current = current["next"]

    current = middle
    while current is not None:
        right = add_last(right, current["info"])
        current = current["next"]

    return left, right

#funcion auxiliar
def _merge(left, right, sort_crit):

    result = new_list()

    node_left = left["first"]
    node_right = right["first"]

    while node_left is not None and node_right is not None:

        if sort_crit(node_left["info"], node_right["info"]):
            result = add_last(result, node_left["info"])
            node_left = node_left["next"]
        else:
            result = add_last(result, node_right["info"])
            node_right = node_right["next"]

    while node_left is not None:
        result = add_last(result, node_left["info"])
        node_left = node_left["next"]

    while node_right is not None:
        result = add_last(result, node_right["info"])
        node_right = node_right["next"]

    return result

def quick_sort(my_list, sort_crit):
    """
    Ordena una lista enlazada simple utilizando el algoritmo recursivo Quick Sort.
    """

    if my_list["first"] is None or my_list["first"]["next"] is None:
        return my_list

    pivot_node = my_list["first"]
    pivot = pivot_node["info"]

    left = new_list()
    right = new_list()
    equal = new_list()

    equal = add_last(equal, pivot)

    current = pivot_node["next"]

    while current is not None:

        value = current["info"]

        if sort_crit(value, pivot):
            left = add_last(left, value)

        elif sort_crit(pivot, value):
            right = add_last(right, value)

        else:
            equal = add_last(equal, value)

        current = current["next"]

    left = quick_sort(left, sort_crit)
    right = quick_sort(right, sort_crit)

    result = new_list()

    current = left["first"]
    while current is not None:
        result = add_last(result, current["info"])
        current = current["next"]

    current = equal["first"]
    while current is not None:
        result = add_last(result, current["info"])
        current = current["next"]

    current = right["first"]
    while current is not None:
        result = add_last(result, current["info"])
        current = current["next"]

    return result