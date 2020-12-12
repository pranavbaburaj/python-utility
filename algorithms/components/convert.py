import json
import os


def to_array(var):
    if isinstance(var, str):
        return [each_element for each_element in str(var)]
    elif isinstance(var, int) or isinstance(var, float):
        return [x for x in str(var)]
    else:
        return []


def dictionaries(item_name, items):
    if isinstance(item_name, list) and isinstance(items, list):
        dict_to_return = {}

        for x in range(len(item_name)):
            dict_to_return[str(item_name[x])] = items[x]
        return dict_to_return
    else:
        raise TypeError(f"Expected type list")
