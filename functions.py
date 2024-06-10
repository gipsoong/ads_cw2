def sort_items_by_title(items):
    """"A function to sort a list of items by its titles"""
    titles = []
    for i in items:
        titles.append(i.title)

    titles.sort()

    return titles


def return_middle_of_list(arg):
    middle_index = (len(arg) - 1) // 2

    return arg[middle_index]


def return_value_of_middle_index(items, title):
    """"
    Iterates through a given list of unsorted items that consists of item objects
    For each iteration, checks if the given title matches with the title of the item in the list
    If it matches - assign the value of the item to value variable, break from the loop and return value
    """
    value = None

    for i in items:
        if title == i.title:
            value = i
            break

    return value


def return_rest_of_items(sorted_list):
    middle_index = (len(sorted_list) - 1) // 2
    sorted_list.pop(middle_index)

    return sorted_list


def insert_loop(root, rest_of_list):
    pass
