from bs4 import BeautifulSoup
from requests import get
from re import findall

# 1. Визначте, в яких аудиторіях проводиться найбільше занять на ФІКТі серед усіх груп і усіх курсів.

# Parse groups list
request = get('https://rozklad.ztu.edu.ua')
html = BeautifulSoup(request.content, "lxml")

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


# 2. Розрахувати кількість занять за місяць у своїй групі
request = get('https://rozklad.ztu.edu.ua/schedule/group/' + 'ВТ-21-1')
html = BeautifulSoup(request.content, "lxml")
vt_21_1_rooms = html.select('.schedule .variative .room')
print(f'The number of ВТ-21-1 classes in 28 days: {len(vt_21_1_rooms) * 2}')


# 3. Визначте, в якій аудиторії частіше всього проходять заняття у вашої групи.

# Parse schedule of ВТ-21-1
vt_21_1_rooms_dict: dict = {}

for room in vt_21_1_rooms:
    room_number = findall(r'\d+', room.text).pop()

    if room_number in vt_21_1_rooms_dict:
        vt_21_1_rooms_dict[room_number] = vt_21_1_rooms_dict[room_number] + 1
    else:
        vt_21_1_rooms_dict[room_number] = 1

# Find top 1 classroom
vt_21_1_rooms_values: list = list(vt_21_1_rooms_dict.values())
vt_21_1_max_index = vt_21_1_rooms_values.index(max(vt_21_1_rooms_values))
print('\nTop 1 room in ВТ-21-1')
print(f'Room: {list(vt_21_1_rooms_dict.keys())[vt_21_1_max_index]}; Classes: {vt_21_1_rooms_values[vt_21_1_max_index]}')
