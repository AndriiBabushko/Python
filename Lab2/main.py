""" Lab 1. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """


# task 1
def task_1(some_int_list):
    some_result_list = []
    for i in range(len(some_int_list)):
        if 1 <= some_int_list[i] <= 3:
            some_result_list.append(some_int_list[i])

    return some_result_list


# task 2
def task_2(year):
    if is_leap_year(year):
        print(f'This year({year}) has 366 days.')
    else:
        print(f'This year({year}) has 365 days.')


def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


# task 1
print('\nTASK 1!!!')
task_1_list = [1, 2, 5, 4, 10, 15, 3]
print(f'Task 1 list: {task_1_list}')
print(f'List of elems that in interval [1; 3]: {task_1(task_1_list)}')

# task 2
print('\nTASK 2!!!')
task_2_year = [2000, 2001, 1932, 1841, 2004, 2014]
for i in range(len(task_2_year)):
    task_2(task_2_year[i])
