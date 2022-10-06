""" Lab 6. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """
import csv
import os
import io
import shutil
from datetime import datetime
from datetime import date
from time import perf_counter

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


# task_1()

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


# task_2()

# task 3
"""
    Завдання 3. Створіть новий файл у текстовому редакторі і напишіть кілька рядків тексту у ньому про можливості 
    Python. Кожен рядок повинен починатися з фрази: «Python можна використати для ...» . Збережіть файл з ім’ям 
    learning_python.txt. Напишіть програму, яка зчитує файл і виводить текст з перебором рядків файла і зі збереженням 
    рядків у списку з подальшим сортуванням списку за довжиною рядків в ньому від найбільшого до найменшого.
"""


def task_3():
    print('\nTASK 3!')

    if not os.path.isdir(r'./task3'):
        os.mkdir('./task3')

    with io.open(r'./task3/learning_python.txt', 'wt', encoding='utf-8') as learning_python_txt:
        learning_python_txt.writelines(
            ["Python можна використати для machine learning.\n",
             "Python можна використати для написання простих скриптів.\n",
             "Python можна використати для програмування веб додатків.\n",
             "Python можна використати для написання особистого телеграм боту.\n"])

    with io.open(r'./task3/learning_python.txt', 'rt', encoding='utf-8') as learning_python_txt:
        python_string_list = []

        for line in learning_python_txt:
            python_string_list.append(line)

        python_string_sorted_list = python_string_list[:]
        python_string_sorted_list.sort(key=len)
        print('\nSorted list:')
        for string in python_string_sorted_list:
            print(string, end="")

        python_string_reversed_sorted_list = python_string_list[:]
        python_string_reversed_sorted_list.sort(key=len, reverse=True)
        print('\nReversed sorted list:')
        for string in python_string_reversed_sorted_list:
            print(string, end="")


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

    if not os.path.isdir(r'./task4'):
        os.mkdir(r'./task4')

    with io.open(r'./task3/learning_python.txt', 'rt', encoding='utf-8') as learning_python_txt:
        python_strings = []

        for string in learning_python_txt:
            python_strings.append(string.split(' '))

        for i in range(0, len(python_strings)):
            python_strings[i][0] = 'C'
            python_strings[i] = " ".join(python_strings[i])

    with io.open(r'./task4/learning_c.txt', 'wt', encoding='utf-8') as true_about_c_txt:
        for c_string in python_strings:
            true_about_c_txt.write(c_string)

    with io.open(r'./task4/learning_c.txt', 'rt', encoding='utf-8') as learning_c_txt:
        for c_string in learning_c_txt:
            print(c_string, end='')
            answer = enter_true_or_false()
            if answer:
                with io.open(r'./task4/true_about_c.txt', 'at', encoding='utf-8') as true_about_c_txt:
                    true_about_c_txt.write(c_string)
            else:
                with io.open(r'./task4/false_about_c.txt', 'at', encoding='utf-8') as false_about_c_txt:
                    false_about_c_txt.write(c_string)

    with io.open(r'./task4/true_about_c.txt', 'rt', encoding='utf-8') as true_about_c_txt_read:
        for c_string in true_about_c_txt_read:
            print(c_string, end='')

    with io.open(r'./task4/false_about_c.txt', 'rt', encoding='utf-8') as false_about_c_txt_read:
        for c_string in false_about_c_txt_read:
            print(c_string, end='')


def enter_true_or_false():
    while True:
        try:
            answer = input("Enter 'true' or 'false' about this statement: ")
            if answer != 'true' and answer != 'false':
                raise ValueError('Value was entered incorrectly!')
            else:
                pass
                if answer == 'true':
                    return True
                elif answer == 'false':
                    return False
        except ValueError as value_err:
            print(f'ERROR! {value_err}')


# task_4()

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

    if not os.path.isdir(r'./task5'):
        os.mkdir(r'./task5')

    task_5_count = enter_count()
    file_create_time = date.today().strftime('%B %d, %Y')

    with io.open(r'./task5/guest_book.txt', 'wt', encoding='utf-8') as guest_book_txt:
        guest_book_txt.write(f'File was created: {file_create_time}\n\n')

        for counter in range(0, task_5_count):
            name_greeting = f'{counter + 1}) Hello, ' + enter_name() + '! '
            message_time = datetime.now().strftime('%H:%M:%S')
            name_greeting += f'Name was entered in time: {message_time}.\n'
            print(name_greeting, end="")
            guest_book_txt.write(name_greeting)

        last_changes_date = date.today().strftime('%B %d, %Y')
        last_changes_time = datetime.now().strftime('%H:%M:%S')
        guest_book_txt.write(f'\nLast changes time: {last_changes_date} {last_changes_time}.\n')


def enter_name():
    while True:
        try:
            name = input('Enter name: ')
            if len(name) < 2:
                raise ValueError('Name\'s length is less than 2!')
            else:
                pass
                return name
        except ValueError as value_err:
            print(f'ERROR! {value_err}')


def enter_count():
    while True:
        try:
            count = int(input('Enter count of names: '))
            if count <= 0:
                raise ValueError('Count names was entered incorrectly!')
            else:
                pass
                return count
        except ValueError as value_err:
            print(f'ERROR! {value_err}')


# task_5()

# task 6
"""
    Завдання 6. Збережіть в текстовому файлі публікацію про Python на 3000 слів англійською мовою. Напишіть програму, 
    що аналізуватиме частоту з якою в тексті зустрічатимуться окремі літери чи слова незалежно від їх регістру. 
    Результат робот програми має виводитись в консоль і зберігатись в окремому файлі з зазначенням часу його створення, 
    часу виконання окремих змін, результатів пошуку і часу, що знадобився на виконання цього пошуку.
"""


def task_6():
    import re
    print('\nTASK 6!')

    with io.open(r'./task6/post_about_python.txt', 'rt', encoding='utf-8') as post_about_python_txt:
        words = re.split(r' |\n|\? |\.|\, |\: |\;', post_about_python_txt.read().lower())

    file_create_date = date.today().strftime('%B %d, %Y')
    file_create_time = datetime.now().strftime('%H:%M:%S')
    with io.open(r'./task6/word_frequency.txt', 'wt', encoding='utf-8') as word_frequency_txt:
        word_frequency_txt.write(f'File was created: {file_create_date} {file_create_time}\n\n')
        print(f'File was created: {file_create_time}\n')

        words_without_duplicates = []
        for string in words:
            if string not in words_without_duplicates:
                words_without_duplicates.append(string)

        print(words_without_duplicates)
        for i in range(0, len(words_without_duplicates)):
            time_started = perf_counter()
            counter = 0
            for j in range(0, len(words)):
                if words_without_duplicates[i] == words[j]:
                    counter += 1
            time_finished = perf_counter()
            write_time = round(time_finished - time_started, 8)
            word_frequency_txt.write(f'"{words[i]}" repeats "{counter}" times. Write time: {write_time}.\n')
            print(f'"{words[i]}" repeats "{counter}" times. Write time: {write_time}.')

        last_changes_date = date.today().strftime('%B %d, %Y')
        last_changes_time = datetime.now().strftime('%H:%M:%S')
        word_frequency_txt.write(f'\nLast changes time: {last_changes_date} {last_changes_time}.\n')
        print(f'\nLast changes time: {last_changes_date} {last_changes_time}.')


# task_6()

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

    if not os.path.isdir(r'./task7'):
        os.mkdir(r'./task7')

    with io.open(r'./task7/marks.lab6.csv', 'rt', encoding='utf-8') as marks_lab6_csv:
        marks_csv = csv.reader(marks_lab6_csv)
        marks = [line for line in marks_csv]

    students_count = len(marks)
    print(f'Total students count who wrote a test: {students_count}')

    students_marks = []
    for i in range(students_count):
        mark_string = marks[i][4].split(',')
        mark_number = float(mark_string[0]) + float(int(mark_string[1]) / 100)
        students_marks.append(mark_number)

    print()
    iterator = 1
    for mark in students_marks:
        print(f'{iterator} student received {mark} mark.')
        iterator += 1

    students_time = []
    for i in range(students_count):
        time = marks[i][3].split(' ')
        if len(time) > 2:
            minutes = int(time[0])
            seconds = int(time[2]) + minutes * 60
        else:
            minutes = int(time[0])
            seconds = minutes * 60
        students_time.append(seconds)

    students_mark_per_min = []
    for i in range(students_count):
        students_mark_per_min.append(round((students_marks[i] / students_time[i]) * 60, 2))

    print()
    iterator = 1
    for average_mark in students_mark_per_min:
        print(f'{iterator} student received {average_mark}/min.')
        iterator += 1

    file_create_date = date.today().strftime('%B %d, %Y')
    file_create_time = datetime.now().strftime('%H:%M:%S')
    with io.open(r'./task7/statistics.txt', 'wt', encoding='utf-8') as statistics_txt:
        statistics_txt.write(f'File was created: {file_create_date} {file_create_time}\n\n')

        student_answers = []
        for answers in marks:
            student_answers.append(answers[5:])

        print()
        iterator = 1
        for answer in student_answers:
            correct_answers = 0
            incorrect_answers = 0

            for i in range(0, len(answer)):
                if answer[i] == '0,50':
                    correct_answers += 1
                else:
                    incorrect_answers += 1

            correct_answers_percentage = round((correct_answers / len(answer)) * 100)
            incorrect_answers_percentage = round((incorrect_answers / len(answer)) * 100)
            statistics_txt.write(f'{iterator} student has {correct_answers_percentage}% of correct answers '
                                 f'and {incorrect_answers_percentage}% of incorrect answers.\n')
            print(f'{iterator} student has {correct_answers_percentage}% of correct answers '
                  f'and {incorrect_answers_percentage}% of incorrect answers.')
            iterator += 1

        print()
        statistics_txt.write('\n')
        top_5_results = []
        students_mark_per_min_copy = students_mark_per_min[:]
        for i in range(0, 5):
            max_average_mark = max(students_mark_per_min_copy)
            top_5_results.append(max_average_mark)
            students_mark_per_min_copy.pop(students_mark_per_min_copy.index(max_average_mark))
            index_of_student = students_mark_per_min.index(top_5_results[i])
            statistics_txt.write(f'Top {i + 1}! {index_of_student} student has {top_5_results[i]}/min mark.\n')
            print(f'Top {i + 1}! {index_of_student} student has {top_5_results[i]}/min mark.')

        last_changes_date = date.today().strftime('%B %d, %Y')
        last_changes_time = datetime.now().strftime('%H:%M:%S')
        statistics_txt.write(f'\nLast changes time: {last_changes_date} {last_changes_time}.\n')


task_7()
