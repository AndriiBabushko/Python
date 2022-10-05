""" Lab 6. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """
import os
import io
import shutil

# task 1
""" 
    Завдання 1. Створіть новий файл numbers.txt у текстовому редакторі і запишіть у нього 10 чисел, кожне з нового 
    рядка. Напишіть програму, яка зчитує ці числа з файлу і обчислює їх суму, виводить цю суму на екран і, водночас, 
    записує цю суму у інший файл з назвою sum_numbers.txt.
"""


def create_numbers_string():
    from random import randint
    new_string = ''

    for new_number in range(10):
        new_string += f'{randint(-100, 100)}\n'

    return new_string


print('TASK 1!')
if not os.path.isdir(r'./task1'):
    os.mkdir(r'./task1')

with io.open(r'./task1/numbers.txt', 'wt', encoding='utf-8') as numbers_txt:
    numbers_txt.write(create_numbers_string())

with io.open(r'./task1/numbers.txt', 'rt', encoding='utf-8') as numbers_txt:
    task_1_sum = 0
    task_1_number_list = []

    for number in numbers_txt:
        try:
            task_1_sum += int(number)
            task_1_number_list.append(int(number))
        except ValueError as err:
            print(f'ERROR! {ValueError}')

    with io.open(r'./task1/sum_numbers.txt', 'wt', encoding='utf-8') as sum_numbers_txt:
        sum_numbers_txt.write(str(task_1_sum))

    print(f'Received numbers from file: {task_1_number_list}')
    print(f'Sum of numbers in file = {task_1_sum}')

# task 2
print('TASK 2!')

# task 3
print('TASK 3!')

# task 4
print('TASK 4!')

# task 5
print('TASK 5!')

# task 6
print('TASK 6!')

# task 7
print('TASK 7!')
