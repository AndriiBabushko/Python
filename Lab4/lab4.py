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


# task_1_list = enter_some_list()
# print(f'Entered list: {task_1_list}')
# print(f'Reversed list: {task_1_output_reverse_list(task_1_list)}')


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


# task_2_list = enter_some_list()
# print(f'Entered list: {task_2_list}')
# print(f'Positive list: {task_2_get_positive_negative_lists(task_2_list)[0]}')
# print(f'Negative list: {task_2_get_positive_negative_lists(task_2_list)[1]}')


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


def create_random_float_list(minRandom, maxRandom):
    newList = []

    for i in range(0, 20):
        newList.append(get_random_float_number(minRandom, maxRandom))

    return newList


print('\nTASK 3!!!')
task_3_list = create_random_float_list(-5, 5)
print(f'Generated list: {task_3_list}')
print(f'Sum of odd numbers: {task_3_get_index_odd_sum_list(task_3_list)}')


# task 4
def task_4():
    return


print('\nTASK 4!!!')


# task 5
def task_5():
    return


print('\nTASK 5!!!')


# task 6
def task_6():
    return


print('\nTASK 6!!!')


# task 7
def task_7():
    return


print('\nTASK 7!!!')


# task 8
def task_8():
    return


print('\nTASK 8!!!')
