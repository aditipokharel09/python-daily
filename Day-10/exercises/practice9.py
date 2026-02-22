def reverse_list(arr):
    new_list = []
    for i in range(len(arr) - 1, -1, -1):
        new_list.append(arr[i])
    return new_list

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst