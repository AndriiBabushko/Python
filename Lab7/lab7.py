""" Lab 7. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """
from datetime import date


# task 1
class Person:
    personCount: int = 0

    def __init__(self, first_name: str, last_name: str, birth_date: str, nickname=None):
        self.firstName = first_name
        self.lastName = last_name
        self.nickname = nickname
        try:
            dates = birth_date.split('-')
            self.birthDate = date(int(dates[0]), int(dates[1]), int(dates[2]))
        except ValueError as valueError:
            print(f'Incorrect birth date! {valueError}')
            self.birth_date = None
        Person.personCount += 1

    def __str__(self) -> str:
        return f'First name: {self.firstName}; Last name: {self.lastName}; Nickname: {self.nickname}; Birth date: {self.birthDate}.'

    def getAge(self) -> str:
        try:
            age = date.today() - self.birthDate
            return f'{int(age.days / 365)}'
        except ValueError as valueError:
            return f'Incorrect birth date! {valueError}'

    def getFullName(self) -> str:
        return f'{self.lastName} {self.firstName}'


def enterPersons(count: int) -> list[Person]:
    counter = 0
    personsList: list[Person] = []

    while count > counter:
        try:
            firstName: str = input("Enter person's first name: ")
            lastName: str = input("Enter person's last name: ")
            birthDate: str = input("Enter person's birth date as 'YYYY-MM-DD': ")
            nickname: str = input("Enter person's nickname(optional): ")
            personsList.append(Person(firstName, lastName, birthDate, nickname))
            count -= 1
        except ValueError as valueError:
            personsList.pop()
            print(f'ERROR! {valueError}')

    return personsList


def enterCount(subject: str) -> int:
    while True:
        try:
            count = int(input(f'Enter {subject}\'s count value: '))
            if int(count):
                pass
                return count
            else:
                raise ValueError('ERROR! Something occurred!')
        except ValueError as valueError:
            print(f'ERROR! {valueError}')


print('TASK 1!!!')
# task_1_persons_list = enterPersons(enterCount('person'))
# print(task_1_persons_list[0])
task_1_first_person: Person = Person('Andrii', 'Babushko', '2004-03-23')
print(f'Class "task_1_first_person" fields:\n{task_1_first_person}')
print(f'Person "{task_1_first_person.getFullName()}" is {task_1_first_person.getAge()} years old.')


# task 2
def modifier(fileName: str) -> list[Person]:
    import io
    import re

    persons: list[Person] = []

    with io.open(f'./{fileName}.txt', 'rt', encoding='utf-8') as personsData:
        for person in personsData:
            data: list[str] = re.split(', |\n', person)
            print(f'This line was read from file:\n{person}')
            persons.append(Person(data[0], data[1], data[2], data[3]))

    with io.open(f'./new_{fileName}.txt', 'wt', encoding='utf-8') as newPersonsData:
        for person in persons:
            written_line: str = f'{person.firstName}, {person.lastName}, {person.getFullName()}, {person.birthDate}, {person.nickname}, {person.getAge()}\n'
            newPersonsData.write(written_line)
            print(f'This line was writen to file:\n{written_line}')

    return persons


print('\nTASK 2!!!')
task_2_person_list: list[Person] = modifier('persons_data')
