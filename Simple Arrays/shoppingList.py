# extract all numbers from the given string items and sum them up.
import re


def shoppingList(items):
    items = re.split(', ;', items)
    s = 0
    for i in items:
        if i.isnumeric():
            s += float(i)
    return s
