# Write a function that takes an iterable (something you can loop through, ie: string, list, or tuple) and produces a dictionary with all distinct elements as the keys, and the number of each element as the value
def count_unique(some_iterable):
    d = {}

    for item in some_iterable:
        d[item] = d.get(item, 0) + 1

    return d

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists
def common_items(list1, list2):
    common_list = []
    i = 0

    while i < len(common_items):

    return []

# Given two lists, (without using the keyword 'in' or the method 'index') return a list of all common items shared between both lists. This time, use a dictionary as part of your solution.
def common_items2(list1, list2):
    common_list = []
    i = 0

    total_list = list1 + list2
    d = count_unique(long_list)

    

    return common_list

