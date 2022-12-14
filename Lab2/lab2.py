""" Lab 2. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """
import math


# task 1
def task_1_interval_int_list(some_int_list):
    some_result_list = []
    for index in range(len(some_int_list)):
        if 1 <= some_int_list[index] <= 3:
            some_result_list.append(some_int_list[index])

    return some_result_list


print('\nTASK 1!!!')
task_1_list = [1, 2, 5, 4, 10, 15, 3]
print(f'Task 1 list: {task_1_list}')
print(f'List of elems that in interval [1; 3]: {task_1_interval_int_list(task_1_list)}')


# task 2
def task_2_year_days(year):
    if is_leap_year(year):
        print(f'This year({year}) has 366 days.')
    else:
        print(f'This year({year}) has 365 days.')


def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


print('\nTASK 2!!!')
task_2_year = [2000, 2001, 1932, 1841, 2004, 2014]
for i in range(len(task_2_year)):
    task_2_year_days(task_2_year[i])


# task 3
def task_3_purchase_discount(purchase):
    if 500 <= purchase < 1000:
        return purchase - purchase * 0.03
    if purchase >= 1000:
        return purchase - purchase * 0.05
    return purchase


print('\nTASK 3!!!')
task_3_purchases = [490, 510, 800, 1100, 2100]
for i in range(len(task_3_purchases)):
    print(f'Purchase: {task_3_purchases[i]}\nFinal price: {task_3_purchase_discount(task_3_purchases[i])}\n')


# task 4
def task_4_min_cosine(angles): return math.cos(min(angles))


print('\nTASK 4!!!')
angles_list = [math.radians(30 / math.pi), math.radians(60 / math.pi), math.radians(90 / math.pi),
               math.radians(120 / math.pi), math.radians(360 / math.pi)]
print(f'Angles list: {angles_list}')
print(f'Min cos in radians from angles list: {task_4_min_cosine(angles_list)}')


# task 5
def task_5_max_sin(angles): return math.sin(max(angles))


print('\nTASK 5!!!')
print(f'Angles list: {angles_list}')
print(f'Max sin in radians from angles list: {task_5_max_sin(angles_list)}')


# task 6
def task_6_isosceles_triangle(sides):
    s = (sides[0] * sides[1]) / 2
    if s % 2 == 0:
        s /= 2
        print(f'The area of the triangle: {s}')
    else:
        print(f"The S({s}), I can\'t divide by 2!")


print('\nTASK 6!!!')
left_right_sides = 1
base_side = 2
for x in range(1, 13, 3):
    task_6_isosceles_triangle([left_right_sides + x, base_side + x])


# task 7
def task_7_english_month(month_number):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    if 1 <= month_number <= 12:
        print(f'{month_number} month is {months[month_number - 1]}')
    else:
        print(f'{month_number} number of month isn\'t in range [1, 12]!')


print('\nTASK 7!!!')
for i in range(0, 14):
    task_7_english_month(i)


# task 8
def task_8_positive_numbers(numbers):
    positive_counter = 0
    for number in numbers:
        if number >= 1:
            positive_counter += 1
    return positive_counter


print('\nTASK 8!!!')
some_numbers = [10, -10, -10.5, -143411, 12032, +120, 1, 0, -1]
print(f'Range of numbers: {some_numbers}')
print(f'Number of positive numbers in range: {task_8_positive_numbers(some_numbers)}')


# task 9
def task_9_sum_some_range(a, b):
    sum_some_range = 0
    for some_num in range(a, b + 1, 1):
        sum_some_range += some_num

    return sum_some_range


print('\nTASK 9!!!')
A = 5
B = 15
print(f'Sum of range from A({A}) to B({B}): {task_9_sum_some_range(A, B)}')


# task 10
def task_10_sum_squares_some_range(a, b):
    sum_squares_some_range = 0
    for some_num in range(a, b + 1, 1):
        sum_squares_some_range += math.pow(some_num, 2)

    return sum_squares_some_range


print('\nTASK 10!!!')
print(f'Sum of squares of range from A({A}) to B({B}): {task_10_sum_squares_some_range(A, B)}')


# task 11
def task_11_arithmetic_mean(a, b):
    arithmetic_mean_sum = 0
    count_nums = 0
    for some_num in range(a, b + 1):
        arithmetic_mean_sum += some_num
        count_nums += 1

    return arithmetic_mean_sum / count_nums


def enter_A_and_B():
    while True:
        a = int(input('Enter A for task 11: '))
        b = int(input('Enter B for task 11: '))
        if a < b:
            break

    return [a, b]


print('\nTASK 11!!!')
some_range = enter_A_and_B()
print(f'Arithmetic mean from A({some_range[0]}) to B({some_range[1]}):'
      f'{task_11_arithmetic_mean(some_range[0], some_range[1])}')


# task 12
def task_12_sum_some_range(a, b):
    sum_some_range = 0
    while a <= b:
        sum_some_range += a
        a += 1

    return sum_some_range


print('\nTASK 12!!!')
print(f'Sum of range from A({A}) to B({B}): {task_12_sum_some_range(A, B)}')


# task 13
def task_13_sum_some_square_range(a):
    sum_some_squares = 0
    for sum_num in range(a, 51, 1):
        sum_some_squares += math.pow(sum_num, 2)

    return sum_some_squares


print('\nTASK 13!!!')
A = 48
print(f'Sum of squares of range from A({A}) to 50: {task_13_sum_some_square_range(A)}')


# task 14
def task_14_find_K(N_number):
    K = N_number
    K_array = [K]
    while math.pow(5, K) > N_number:
        K -= 1
        K_array.append(K)

    return min(K_array)


def enter_N():
    while True:
        some_N = int(input('Enter N: '))
        if some_N > 1:
            break

    return some_N


print('\nTASK 14!!!')
N = enter_N()
print(f'Some K from N({N}): {task_14_find_K(N)}')


# task 15
def task_15_find_number_greater_n(n):
    for number in range(1, n, 1):
        some_number = math.pow(number, 2)
        if some_number > n:
            return some_number
        else:
            continue

    return n


print('\nTASK 15!!!')
N = enter_N()
print(f'The first number that greater than n: {task_15_find_number_greater_n(N)}')


# task 16
def task_16_find_number_greater_n(n):
    some_number = 1
    iterator = 2
    while some_number < n:
        some_number = math.pow(iterator, 2) + 1
        iterator += 1

    return some_number


print('\nTASK 16!!!')
N = enter_N()
print(f'The first number that greater than n: {task_16_find_number_greater_n(N)}')
