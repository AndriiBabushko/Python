""" Lab 5. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """


# task 1
def task_1_get_rectangles_areas(rectangles_sides):
    areas = []

    for i in range(0, len(rectangles_sides)):
        areas.append(rectangles_sides[i][0] * rectangles_sides[i][1])

    return areas


def enter_rectangles_sides(counter):
    rectangles_sides = []

    while counter != 0:
        try:
            side_a = float(input(f'Enter length of side a: '))
            side_b = float(input(f'Enter length of side b: '))
            rectangles_sides.append([side_a, side_b])
            if side_a < 0 or side_b < 0:
                raise ValueError(f'Sides менше 0!')
            else:
                pass
                print('Sides were entered correctly!')
                counter -= 1
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

    while counter != 0:
        try:
            leg_a = float(input(f'Enter leg a: '))
            leg_b = float(input(f'Enter leg b: '))
            right_triangles_legs.append([leg_a, leg_b])
            if leg_a < 0 or leg_b < 0:
                raise ValueError(f'Legs are less than 0!')
            else:
                pass
                print('Legs were entered correctly!')
                counter -= 1
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


# task_2_right_triangles_legs = enter_right_triangles_legs(2)
# print(f'List of right triangle legs: {task_2_right_triangles_legs}')
# task_2_hypotenuses = task_2_get_right_triangles_hypotenuses(task_2_right_triangles_legs)
# compare_hypotenuses(task_2_hypotenuses)


# task 3
def check_if_point_is_in_circle(checked_point, circle_points_and_radius):
    equation = (checked_point[0] - circle_points_and_radius[0]) ** 2 + (
            checked_point[1] - circle_points_and_radius[1]) ** 2

    # print(f'Radius ^2: {circle_points_and_radius[2] ** 2}')
    # print(f'Equation: {equation}')
    if (circle_points_and_radius[2] ** 2) == equation:
        return True
    return False


def enter_circle_center_points_and_radius():
    point_a = 0
    point_b = 0
    circle_radius = 0

    while True:
        try:
            point_a = float(input(f'Enter circle center point a: '))
            point_b = float(input(f'Enter circle center point b: '))
            circle_radius = float(input(f'Enter radius: '))
            if circle_radius < 0:
                raise ValueError(f'Radius is less than 0!')
            else:
                pass
                print('Center circle points and radius were entered correctly!')
                break
        except ValueError as value_error:
            print('ERROR:', value_error)

    return [point_a, point_b, circle_radius]


def enter_some_point(point):
    point_a = 0
    point_b = 0

    while True:
        try:
            if point == 0:
                point_a = float(input(f'Enter point p1 of P: '))
                point_b = float(input(f'Enter point p2 of P: '))
            if point == 1:
                point_a = float(input(f'Enter point f1 of F: '))
                point_b = float(input(f'Enter point f2 of F: '))
            if point == 2:
                point_a = float(input(f'Enter point l1 of L: '))
                point_b = float(input(f'Enter point l2 of L: '))
            break
        except ValueError as value_error:
            print('ERROR:', value_error)

    return [point_a, point_b]


print('\nTASK 3!!!')


# counter_point_in_circle = 0
# counter_point_out_of_circle = 0
# task_3_circle_center_and_radius = enter_circle_center_points_and_radius()
# print(f'Center point O({task_3_circle_center_and_radius[0]}, {task_3_circle_center_and_radius[1]}).'
#       f' Radius: {task_3_circle_center_and_radius[2]}')
# for i in range(0, 3):
#     task_3_some_point = enter_some_point(i)
#     if check_if_point_is_in_circle(task_3_some_point, task_3_circle_center_and_radius):
#         counter_point_in_circle += 1
#     else:
#         counter_point_out_of_circle += 1
#
# print(f'Count of points which are in circle: {counter_point_in_circle}')
# print(f'Count of points which are out of circle: {counter_point_out_of_circle}')


# task 4
def enter_quadrangle_data():
    from math import sqrt
    quadrangle = {
        'x': 0,
        'y': 0,
        'z': 0,
        't': 0,
        'diagonal': 0
    }

    while True:
        try:
            quadrangle['x'] = float(input('Enter x: '))
            quadrangle['y'] = float(input('Enter y: '))
            quadrangle['z'] = float(input('Enter z: '))
            quadrangle['t'] = float(input('Enter t: '))
            quadrangle['diagonal'] = sqrt(quadrangle['x'] ** 2 + quadrangle['y'] ** 2)
            if quadrangle['x'] < 0 or quadrangle['y'] < 0 or quadrangle['z'] < 0 or quadrangle['t'] < 0:
                raise ValueError(f'Some side length is less than 0!')
            else:
                pass
                print('Sides length were entered correctly!')
                break
        except ValueError as value_error:
            print('ERROR:', value_error)

    return quadrangle


def get_first_square(x, y):
    return x * y * 0.5


def get_second_square(d, z, t):
    from math import sqrt

    p = (z + t + d) / 2

    return sqrt(p * (p - z) * (p - t) * (p - d))


print('\nTASK 4!!!')
task_4_quadrangle = enter_quadrangle_data()
task_4_square_of_quadrangle = round(
    get_first_square(task_4_quadrangle['x'], task_4_quadrangle['y']) +
    get_second_square(task_4_quadrangle['diagonal'], task_4_quadrangle['z'], task_4_quadrangle['t'])
    , 2)
print(f'Square of quadrangle: {task_4_square_of_quadrangle}')

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
