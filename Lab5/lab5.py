""" Lab 5. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """


# task 1
def task_1_get_rectangles_areas(rectangles_sides):
    areas = []

    for i in range(0, len(rectangles_sides)):
        areas.append(rectangles_sides[i][0] * rectangles_sides[i][1])

    return areas


def enter_rectangles_sides(counter):
    rectangles_sides = []

    while True:
        try:
            side_a = float(input(f'Enter length of side a: '))
            side_b = float(input(f'Enter length of side b: '))
            rectangles_sides.append([side_a, side_b])
            if side_a < 0 or side_b < 0:
                raise ValueError(f'Сторони менше 0!')
            else:
                pass
                print('Сторони введено правильно!')
                counter -= 1
            if counter == 0:
                break
        except ValueError as value_error:
            rectangles_sides.pop()
            print('ERROR:', value_error)

    return rectangles_sides


print('\nTASK 1!!!')


# task_1_rectangles_sides = enter_rectangles_sides(3)
# print(f'List of rectangles sides: {task_1_rectangles_sides}')
# task_1_rectangles_areas = task_1_get_rectangles_areas(task_1_rectangles_sides)
# for rectangle in range(0, len(task_1_rectangles_areas)):
#     print(f'{rectangle + 1} rectangle\'s area: {task_1_rectangles_areas[rectangle]}')


# task 2
def task_2_get_right_triangles_hypotenuses(right_triangles_legs):
    hypotenuses = []

    for i in range(0, len(right_triangles_legs)):
        hypotenuses.append(round((right_triangles_legs[i][0] ** 2 + right_triangles_legs[i][1] ** 2) ** 0.5, 2))

    return hypotenuses


def enter_right_triangles_legs(counter):
    right_triangles_legs = []

    while True:
        try:
            leg_a = float(input(f'Enter leg a: '))
            leg_b = float(input(f'Enter leg b: '))
            right_triangles_legs.append([leg_a, leg_b])
            if leg_a < 0 or leg_b < 0:
                raise ValueError(f'Сторони менше 0!')
            else:
                pass
                print('Сторони введено правильно!')
                counter -= 1
            if counter == 0:
                break
        except ValueError as value_error:
            right_triangles_legs.pop()
            print('ERROR:', value_error)

    return right_triangles_legs


def compare_hypotenuses(hypotenuses):
    for i in range(0, len(hypotenuses) - 1):
        if hypotenuses[i] > hypotenuses[i + 1]:
            print(f'Hypotenuse №{i + 1}({hypotenuses[i]}) > Hypotenuse №{i + 2}({hypotenuses[i + 1]})')
        else:
            print(f'Hypotenuse №{i + 1}({hypotenuses[i]}) < Hypotenuse №{i + 2}({hypotenuses[i + 1]})')


print('\nTASK 2!!!')
task_2_right_triangles_legs = enter_right_triangles_legs(2)
print(f'List of right triangle legs: {task_2_right_triangles_legs}')
task_2_hypotenuses = task_2_get_right_triangles_hypotenuses(task_2_right_triangles_legs)
compare_hypotenuses(task_2_hypotenuses)

# task 3

print('\nTASK 3!!!')

# task 4

print('\nTASK 4!!!')

# task 5

print('\nTASK 5!!!')

# task 6

print('\nTASK 6!!!')

# task 7

print('\nTASK 7!!!')

# task 8

print('\nTASK 8!!!')

# task 9

print('\nTASK 9!!!')
