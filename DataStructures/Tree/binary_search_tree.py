
from DataStructures.Tree import bst_node as node
from DataStructures.List import array_list as lt

def put(my_bst,key,value):
    my_bst["root"] = insert_node(my_bst["root"],key,value)
    return my_bst
    
    
def insert_node(root, key, value):
    if root is None:
        return node.new_node(key,value)
    root_key = node.get_key(root)
    
    if key < root_key:
        root["left"] = insert_node(root["left"],key,value)
    elif key > root_key:
        root["right"] = insert_node(root["right"],key,value)
    else:
        root["value"] = value
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])    
        
    return root
    
def get(my_bst, key):
    if my_bst is None or my_bst["root"] is None:
        return None
    result = get_node(my_bst["root"],key)
    
    if result is None:
        return None
    return node.get_value(result)
    
def get_node(root, key):
    if root is None:
        return None
    root_key = node.get_key(root)
    
    if key == root_key:
        return root
    elif key < root_key:
        return get_node(root["left"],key)
    elif key > root_key:
        return get_node(root["right"],key)
    
def remove(my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst
    
def remove_node(root, key):
    if root is None:
        return None
    root_key = node.get_key(root)
    
    if key < root_key:
        root["left"] = remove_node(root["left"],key)
    elif key > root_key:
        root["right"] = remove_node(root["right"],key)
    else:
        if root["left"] is None:
            return root["right"]
        if root["right"] is None:
            return root["left"]

        temporal = root
        min_node = get_min_node(temporal["right"])
        root = min_node
        root["right"] = delete_min_tree(temporal["right"])
        root["left"] = temporal["left"]
        
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root
    
def contains(my_bst, key):
    return get(my_bst,key) is not None
    
def size(my_bst):
    if my_bst is None or my_bst["root"] == None:
        return 0
    return my_bst["root"]["size"]
    
def size_tree(root):
    if root is None:
        return 0
    return root["size"]
    
def is_empty(my_bst):
    return size(my_bst) == 0
    
def key_set(my_bst):
    result = lt.new_list()
    key_set_tree(my_bst["root"],result)
    return result
    
def key_set_tree(root,list_keys):
    if root is None:
        return
    
    key_set_tree(root["left"],list_keys)
    lt.add_last(list_keys,node.get_key(root))
    key_set_tree(root["right"],list_keys)
    
def value_set(my_bst):
    result = lt.new_list()
    value_set_tree(my_bst["root"],result)
    return result
    
def value_set_tree(root,list_values):
    if root is None:
        return
    
    value_set_tree(root["left"],list_values)
    lt.add_last(list_values,node.get_value(root))
    value_set_tree(root["right"],list_values)
    
def get_min(my_bst):
    if my_bst is None or my_bst["root"] is None:
        return None
    
    min_node = get_min_node(my_bst["root"])
    return node.get_key(min_node)
    
def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return root
    return get_min_node(root["left"])
    
def get_max(my_bst):
    if my_bst is None or my_bst["root"] is None:
        return None
    
    max_node = get_max_node(my_bst["root"])
    return node.get_key(max_node)

def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root
    return get_max_node(root["right"])

def delete_min(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst
    
def delete_min_tree(root):
    if root["left"] is None:
        return root["right"]
    
    root["left"] = delete_min_tree(root["left"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    
    return root
    
def delete_max(my_bst):
    if my_bst["root"] is not None:
        my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root["right"] is None:
        return root["left"]
    
    root["right"] = delete_min_tree(root["right"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    
    return root

def height(my_bst):
    return height_tree(my_bst["root"])
    
def height_tree(root):
    if root is None:
        return 1
    return 1 + max(height_tree(root["left"]),height_tree(root["right"]))
    
def keys(my_bst, key_initial, key_final):
    result = lt.new_list()
    keys_range(my_bst["root"],key_initial,key_final,result)
    return result
    
def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return
    key = node.get_key(root)
    
    if key > key_initial:
        keys_range(root["left"],key_initial,key_final,list_key)
    if key_initial <= key <= key_final:
        lt.add_last(list_key,key)
    if key < key_final:
        keys_range(root["right"],key_initial,key_final,list_key)
    
def values(my_bst, key_initial, key_final):
    result = lt.new_list()
    values_range(my_bst["root"],key_initial,key_final,result)
    return result
    
def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return
    key = node.get_key(root)
    
    if key > key_initial:
        values_range(root["left"],key_initial,key_final,list_value)
    if key_initial <= key <= key_final:
        lt.add_last(list_value,key)
    if key < key_final:
        values_range(root["right"],key_initial,key_final,list_value)