# task 1
print('TASK 1!!!\n')
firstInt = int(input('Enter first int number: '))
secondInt = int(input('Enter second int value: '))
firstFloat = float(input('Enter first float number: '))
secondFloat = float(input('Enter second float number: '))
firstComplex = complex(input('Enter first complex number: '))
secondComplex = complex(input('Enter second complex number: '))

print('\nfirstInt = ' + str(firstInt) + '; secondStr = ' + str(secondInt) + ';')
print('firstFloat = ' + str(firstFloat) + '; secondFloat = ' + str(secondFloat) + ';')
print('firstComplex = ' + str(firstComplex) + '; secondComplex = ' + str(secondComplex) + ';')

# task 2
print('\nTASK 2!!!\n')

# intList
intResultList = [int(firstInt + secondInt), int(firstInt - secondInt), int(firstInt * secondInt),
                 int(firstInt / secondInt), int(firstInt ** secondInt), int(firstInt // secondInt),
                 int(firstInt % secondInt)]
print('Int result list: ' + str(intResultList))

# floatList
floatResultList = [float(firstFloat + secondFloat), float(firstFloat - secondFloat),
                   float(firstFloat * secondFloat), float(firstFloat / secondFloat),
                   float(firstFloat ** secondFloat), float(firstFloat // secondFloat),
                   float(firstFloat % secondFloat)]
print('Float result list: ' + str(floatResultList))

# complexList
complexResultList = [complex(firstComplex + secondComplex), complex(firstComplex - secondComplex),
                     complex(firstComplex * secondComplex), complex(firstComplex / secondComplex)]
print('Complex result list: ' + str(complexResultList))

# result list
resultList = [intResultList, floatResultList, complexResultList]
print('Result list: ' + str(resultList))

# task 3
print('\nTASK 3!!!\n')

# amount of int list items
print('Amount of int list items: ' + str(len(intResultList)))
evenListElements = []

# add even items to even list
for number in intResultList:
    if number % 2 == 0:
        evenListElements.append(number)
print('Even list elements: ' + str(evenListElements))

# task 4
print('\nTASK 4!!!\n')

# change places 2 and 5 elements of the int list
print('Int list before changes: ' + str(intResultList))
intResultList[1], intResultList[4] = intResultList[4], intResultList[1]
print('Int list after changes: ' + str(intResultList))

# task 5
print('\nTASK 5!!!\n')

name = input('Enter name and surname: ')
print('Лабораторну роботу №1 виконав: ' + str(name) + '.\nПід час виконання лабораторної роботи було отримано навички '
                                                      'з написання простої програми на мові Python, використовуючи '
                                                      'прості конструкції та оператори цієї мови.')
