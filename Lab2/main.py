""" Lab 1. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """


# task 1
def task_1(some_int_list):
    some_result_list = []
    for i in range(len(some_int_list)):
        if 1 <= some_int_list[i] <= 3:
            some_result_list.append(some_int_list[i])

    return some_result_list


task_1_list = [1, 2, 5, 4, 10, 15, 3]
print(f'Task 1 list: {task_1_list}')
print(f'List of elems that in interval [1; 3]: {task_1(task_1_list)}')
