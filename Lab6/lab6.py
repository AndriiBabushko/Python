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


def task_1():
    print('\nTASK 1!')
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


def create_numbers_string():
    from random import randint
    new_string = ''

    for new_number in range(10):
        new_string += f'{randint(-100, 100)}\n'

    return new_string


task_1()

# task 2
"""
    Завдання 2. Реалізуйте програму, яка зчитує довільну кількість цілих чисел, що вводяться з командного рядка, і 
    записує у текстовий файл інформацію, щодо парності або непарності чисел.
"""


def task_2():
    print('\nTASK 2!')
    task_2_enter_count = int(input('Enter how much numbers you want to enter: '))
    task_2_number_list = task_2_enter_some_numbers(task_2_enter_count)

    if not os.path.isdir(r'./task2'):
        os.mkdir(r'./task2')

    with io.open(r'./task2/even_or_odd_numbers.txt', 'wt', encoding='utf-8') as even_or_odd_numbers_txt:
        for number in task_2_number_list:
            if number % 2 == 0:
                even_or_odd_numbers_txt.write(f'{number} is even number!\n')
            else:
                even_or_odd_numbers_txt.write(f'{number} is odd number!\n')

    with io.open(r'./task2/even_or_odd_numbers.txt', 'rt', encoding='utf-8') as even_or_odd_numbers_txt:
        for line in even_or_odd_numbers_txt:
            print(line, end="")


def task_2_enter_some_numbers(count):
    numbers_list = []

    while count != 0:
        try:
            int_number = int(input('Enter value: '))
            numbers_list.append(int_number)
            count -= 1
        except ValueError as value_error:
            numbers_list.pop()
            print('ERROR:', value_error)

    return numbers_list


task_2()

# task 3
"""
    Завдання 3. Створіть новий файл у текстовому редакторі і напишіть кілька рядків тексту у ньому про можливості 
    Python. Кожен рядок повинен починатися з фрази: «Python можна використати для ...» . Збережіть файл з ім’ям 
    learning_python.txt. Напишіть програму, яка зчитує файл і виводить текст з перебором рядків файла і зі збереженням 
    рядків у списку з подальшим сортуванням списку за довжиною рядків в ньому від найбільшого до найменшого.
"""


def task_3():
    print('\nTASK 3!')


task_3()

# task 4
"""
    Завдання 4. Прочитайте кожен рядок зі створеного у попередньому завданні файла learning_python.txt і замініть 
    слово Python назвою іншої мови, наприклад C при виведенні на екран. Отриманий файл має бути створений в новому 
    каталозі, що розміщується в поточному. Відкрийте файл пострічково і дайте можливість користувачеві визначити які 
    змінені фрази є актуальними, наприклад для мови С, а які ні. Всі хибні твердження запишіть в інший файл, а істинні 
    – в поточний.
"""


def task_4():
    print('\nTASK 4!')


task_4()

# task 5
"""
    Завдання 5. Створіть порожній файл guest_book.txt у текстовому редакторі. Напишіть програму, яка запитує у 
    користувачів імена. При введенні кожного імені виведіть на екран рядок з вітанням для користувача і запишіть 
    рядок вітання у файл з ім’ям guest_book.txt. Простежте за тим, щоб кожне повідомлення розміщувалося в окремому 
    рядку файла з зазначенням часу внесення цього повідомлення. Передбачте зазначення в файлі часу його створення і 
    вказання в ньому часу останніх внесених змін
"""


def task_5():
    print('\nTASK 5!')


task_5()

# task 6
"""
    Завдання 6. Збережіть в тектовому файлі публікацію про Python на 3000 слів англійською мовою. Напишіть програму, 
    що аналізуватиме частоту з якою в тексті зустрічастимуться окремі літери чи слова незалежно від їх регістру. 
    Результат робот програми має виводитись в консоль і зберігатись в окремому файлі з зазначенням часу його стоврення, 
    часу виконнання окремих змін, результатів пошкуку і часу, що знадовся на виконнання цього пошуку.
"""


def task_6():
    print('\nTASK 6!')


task_6()

# task 7
"""
    Завдання 7. Завантажте файл marks.csv і визначте кількість студентів, що проходили тестування. Виведіть інформацію 
    про те яку оцінку набрали відповідна кільксть студентів. Виведіть інформацію яку середню оцінку отримував студент 
    за певний час виконання КМР (крок – 1 хв). Створіть текстовий файл і запишіть в нього статистику по правильним 
    відповідям для кожного окремого питання (який відсоток правильних і неправильних відповідей на питання дали 
    студенти). В цей же файл внесіть інформацію про 5 найкращих оцінок в співвідношенні оцінка/час витрачений 
    складання КМР.
"""


def task_7():
    print('\nTASK 7!')


task_7()
