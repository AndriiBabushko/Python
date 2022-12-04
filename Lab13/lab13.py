from bs4 import BeautifulSoup
from requests import get
from re import findall

request = get('https://rozklad.ztu.edu.ua')
html = BeautifulSoup(request.content, "lxml")

# Визначте, в яких аудиторіях проводиться найбільше занять на ФІКТі серед усіх груп і усіх курсів.

# Parse groups list
groups_list: list[str] = []
groups = html.select('body > div:nth-child(15) .collection .collection-item')
for group in groups:
    groups_list.append(group.text)

# Parse rooms
rooms_dict: dict = {}
for group in groups_list:
    request = get('https://rozklad.ztu.edu.ua/schedule/group/' + str(group))
    html = BeautifulSoup(request.content, "lxml")
    rooms = html.select('.schedule .variative .room')

    for room in rooms:
        room_number = findall(r'\d+', room.text).pop()

        if room_number in rooms_dict:
            rooms_dict[room_number] = rooms_dict[room_number] + 1
        else:
            rooms_dict[room_number] = 1

print(rooms_dict)

# Find top 10 max rooms
top_10_rooms: dict = {}
rooms_keys: list = list(rooms_dict.keys())
rooms_values: list = list(rooms_dict.values())
for i in range(0, 10):
    max_index = rooms_values.index(max(rooms_values))

    top_10_rooms[rooms_keys[max_index]] = rooms_values[max_index]

    rooms_keys.pop(max_index)
    rooms_values.pop(max_index)

print('Top 10 rooms in FIKT')
for key, value in top_10_rooms.items():
    print(f'Room: {key}; Classes: {value}')

# Визначте, в якій аудиторії частіше всього проходять заняття у вашої групи.


