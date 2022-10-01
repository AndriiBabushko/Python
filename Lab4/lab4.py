""" Lab 4. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """


# task 1
def task_1_output_reverse_list(someList):
    someList.reverse()
    return someList


def enter_some_list():
    print('Enter 0 to end input numbers.')
    newList = []
    while True:
        number = float(input('Enter some number: '))
        if number == 0:
            return newList
        else:
            newList.append(number)


print('\nTASK 1!!!')
task_1_list = enter_some_list()
print(f'Entered list: {task_1_list}')
print(f'Reversed list: {task_1_output_reverse_list(task_1_list)}')


# task 2
def task_2_get_positive_negative_lists(someList):
    positive_list = []
    negative_list = []
    for number in someList:
        if number >= 0:
            positive_list.append(number)
        else:
            negative_list.append(number)
    return [positive_list, negative_list]


print('\nTASK 2!!!')
task_2_list = enter_some_list()
print(f'Entered list: {task_2_list}')
print(f'Positive list: {task_2_get_positive_negative_lists(task_2_list)[0]}')
print(f'Negative list: {task_2_get_positive_negative_lists(task_2_list)[1]}')


# task 3
def task_3_get_index_odd_sum_list(someList):
    odd_sum = 0

    for i in range(0, len(someList)):
        if i % 2 != 0:
            odd_sum += someList[i]

    return odd_sum


def get_random_float_number(minRandom, maxRandom):
    import random as random
    return round((random.random() * (maxRandom - minRandom) + minRandom), 2)


def create_random_float_list(n, minRandom, maxRandom):
    newList = []

    for i in range(0, n):
        newList.append(get_random_float_number(minRandom, maxRandom))

    return newList


print('\nTASK 3!!!')
task_3_list = create_random_float_list(20, -5, 5)
print(f'Generated list: {task_3_list}')
print(f'Sum of odd numbers: {task_3_get_index_odd_sum_list(task_3_list)}')


# task 4
def get_max_elem_list(some_list):
    return max(some_list)


def get_max_index_list(some_list):
    return some_list.index(max(some_list))


def get_random_int_number(min_random, max_random):
    import random as random
    return round((random.random() * (max_random - min_random) + min_random))


def create_random_int_list(n, min_random, max_random):
    new_list = []

    for i in range(0, n):
        new_list.append(get_random_int_number(min_random, max_random))

    return new_list


def task_5_get_sorted_odd_list(some_list):
    odd_number_list = []

    for number in some_list:
        if number % 2 != 0:
            odd_number_list.append(number)

    odd_number_list.sort(reverse=True)
    return odd_number_list


print('\nTASK 4!!!')
task_4_list = create_random_int_list(30, -100, 100)
print(f'Generated list: {task_4_list}')
print(f'Max value {get_max_elem_list(task_4_list)} found in index {get_max_index_list(task_4_list)}')
print(f'Odd reverse sorted list: {task_5_get_sorted_odd_list(task_4_list)}')


# task 5
def task_5_get_negative_pairs(some_list):
    negative_pairs_counter = 0
    for i in range(0, len(some_list) - 1):
        if some_list[i] < 0 and some_list[i + 1] < 0:
            negative_pairs_counter += 1
            print(f'{negative_pairs_counter}) {some_list[i]} in {i} and {some_list[i + 1]} in {i + 1}')


print('\nTASK 5!!!')
task_5_list = create_random_int_list(30, -100, 100)
print(f'Generated list: {task_5_list}')
task_5_get_negative_pairs(task_5_list)


# task 6
def task_6_get_squares_list_lower_than_max(some_list):
    squares_list = []
    max_number = max(some_list)

    for number in some_list:
        if number < max_number:
            squares_list.append(number ** 2)

    squares_list.sort(reverse=True)
    return squares_list


print('\nTASK 6!!!')
task_6_list = create_random_int_list(5, -100, 100)
print(f'Generated list: {task_6_list}')
print(f'New list with squared numbers lower than max:\n{task_6_get_squares_list_lower_than_max(task_6_list)}')


# task 7
def task_7_get_min_abs_elem(some_list):
    return abs(min(some_list))


def create_random_int_float_list(n, min_random, max_random):
    import random as random

    new_list = []
    bools = [True, False]

    for i in range(0, n):
        bool_type = bools[random.randint(0, 1)]
        if bool_type:
            new_list.append(get_random_int_number(min_random, max_random))
        else:
            new_list.append(get_random_float_number(min_random, max_random))

    new_list.sort()
    return new_list


print('\nTASK 7!!!')
task_7_list = create_random_int_float_list(30, -100, 100)
print(f'Generated list: {task_7_list}')
print(f'Min abs element in list: {task_7_get_min_abs_elem(task_7_list)}')


# task 8
def task_8_create_3_lists_of_10_elems(some_list):
    for i in range(0, len(some_list)):
        some_list[i] = abs(some_list[i])

    print(some_list)
    first_10_elems = some_list[:10]
    first_10_elems.sort()
    second_10_elems = some_list[10:20]
    second_10_elems.sort()
    third_10_elems = some_list[20:30]
    third_10_elems.sort()

    return [first_10_elems, second_10_elems, third_10_elems]


print('\nTASK 8!!!')
task_8_list = create_random_int_float_list(30, -100, 100)
print(f'Generated list: {task_8_list}')
three_lists_of_10_elems = task_8_create_3_lists_of_10_elems(task_8_list)
print(f'First 10 elems: {three_lists_of_10_elems[0]}')
print(f'Second 10 elems: {three_lists_of_10_elems[1]}')
print(f'Third 10 elems: {three_lists_of_10_elems[2]}')
