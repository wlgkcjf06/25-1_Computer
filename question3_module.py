def move_cusor_right(input_list, cursor):
    cursor += 1
    if cursor >= len(input_list):
        cursor = 0
    return cursor

def move_cusor_left(input_list, cursor):
    cursor -= 1
    if cursor < 0:
        cursor = len(input_list) - 1
    return cursor
    
def is_empty(input_list):
    if len(input_list) == 0:
        return True
    else:
        return
    
def is_full(input_list):
    if len(input_list) == 10:
        return True
    else:
        return False

def append_front(input_list, value):
    input_list.insert(0,value)
    return input_list

def append_back(input_list, value):
    input_list.append(value)
    return input_list

def remove_front(input_list):
    input_list.pop(0)
    return input_list

def remove_back(input_list):
    input_list.pop(len(input_list)-1)
    return input_list

def insert(input_list, value, cursor):
    input_list.insert(cursor,value)
    return input_list

def delete(input_list, cursor):
    input_list.pop(cursor)
    return input_list

