# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []

    for i in some_list:
        if i % 2 != 0:
            new_list.append(i)

    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []

    for i in some_list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []

    for i in word_list:
        if len(i) >= 4:
            new_list.append(i)

    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    small = some_list[0]

    for i in some_list:
        if i < small:
            small = i

    return small

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    large = some_list[0]

    for i in some_list:
        if i > large:
            large = i

    return large

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []

    for i in some_list:
        new_list.append(i / 2.0)

    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []

    for i in word_list:
        new_list.append(len(i))

    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    i = 0
    total = 0

    while i < len(numbers):
        total = total + numbers[i]

        i += 1

    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    i = 0
    total = 1

    while i < len(numbers):
        total = total * numbers[i]

        i += 1

    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    i = 0

    while i <= len(string_list) - 1:
        if i == 0:
            sentence = string_list[i]
        else:
            sentence = sentence + " " + string_list[i]
        i += 1

    return sentence

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    average = sum_numbers(numbers) / float(len(numbers))

    return average
