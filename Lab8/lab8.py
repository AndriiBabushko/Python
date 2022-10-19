""" Lab 8. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """

# task 1
"""
1.	Напишіть клас Bank для опису простих операції з вашим банківським рахунком: покласти на рахунок, зняти з рахунку, переглянути рахунок. При створенні екземпляру класу, екземпляр
    отримує атрибут __balance з певним значенням. Клас повинен містити методи для додавання коштів на рахунок і знімання з рахунку, за умови, що на рахунку достатньо коштів.
"""


class Bank:
    def __init__(self, balance: float):
        self.__balance = balance

    def deposit_money(self, deposit_money):
        self.__balance += deposit_money

    def withdraw_money(self, withdrawal_money):
        if self.__balance - withdrawal_money < 0:
            print('Not enough money!')
        else:
            self.__balance -= withdrawal_money

    def __str__(self):
        return f'You have {self.__balance} UAH!'

    def get_balance(self):
        return self.__balance


print('TASK 1!!!')
task_1_bank: Bank = Bank(1000)
print(task_1_bank)
print('We are adding to your bank 500 UAH!')
task_1_bank.deposit_money(500)
print(f'Now you have {task_1_bank.get_balance()} UAH!')
print('Try to withdraw 1600 UAH!')
task_1_bank.withdraw_money(1600)
print('Try to withdraw 500 UAH!')
task_1_bank.withdraw_money(500)
print(f'Now you have {task_1_bank.get_balance()} UAH!')

# task 2
"""
2.	Напишіть клас Coin, який описує монету, яку можна підкидати. При створенні екземпляру класу, екземпляр отримує атрибут __sideup зі значенням heads або tails. У класі визначте
    метод toss, який випадково визначає результат підкидання монети - орел чи решка. Створіть екземпляр класу і виведіть на екран n підкидань монети.
"""


class Coin:
    def __init__(self):
        self.__side_up = 'Heads'

    def toss(self):
        from random import randint
        rand_side: int = randint(0, 1)
        if rand_side == 1:
            print('Tossed heads!')
            self.__side_up = 'Heads'
        else:
            print('Tossed tails!')
            self.__side_up = 'Tails'


print('\nTASK 2!!!')
task_2_coin: Coin = Coin()
for tossed in range(0, 5):
    print(f'{tossed + 1} toss...')
    task_2_coin.toss()

# task 3
"""
3.	Напишіть клас Car, який надає для створених екземплярів такі атрибути даних автомобіля: марку виготовлення автомобіля, модель автомобіля, рік автомобіля, швидкість
    (початкове значення 0). Клас також повинен мати наступні методи: accelerate (метод повинен щоразу додавати 5 до значення атрибуту даних про швидкість), 
    brake (метод повинен віднімати 5 від значення атрибута даних швидкості кожного разу, коли він викликається), get_speed (метод повинен повернути поточну швидкість).
    Створіть екземпляр класу Car і викличте метод accelerate п’ять разів. Після кожного виклику методу accelerate отримайте поточну швидкість автомобіля і надрукуйте її значення.
    Потім викличте метод brake п’ять разів. Після кожного виклику методу brake отримайте поточну швидкість автомобіля та надрукуйте її значення.
"""
print('\nTASK 3!!!')

# task 4
"""

"""
print('\nTASK 4!!!')

# task 5
"""

"""
print('\nTASK 5!!!')

# task 6
"""

"""
print('\nTASK 6!!!')

# task 7
"""

"""
print('\nTASK 7!!!')

# task 8
"""

"""
print('\nTASK 8!!!')
