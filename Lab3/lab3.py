""" Lab 3. Python. Andrii Babushko. Repository: https://github.com/AndriiBabushko/Python """


# task 1
def task_1_find_word_in_text(text, searching_letter):
    count_searching_letters = 0
    searching_letter = searching_letter.capitalize()
    split_text = text.split(' ')
    for i in range(0, len(split_text)):
        split_text[i] = split_text[i].capitalize()
        if split_text[i][0] == searching_letter:
            count_searching_letters += 1

    return count_searching_letters


print('\nTASK 1!!!')
task_1_some_text = 'lorem ipsum lorem Ipsum dolor Dit amet, Consectetur adipiscing elit.'
print(f'Task 1 text: "{task_1_some_text}"')
task_1_some_searching_letter = str(input('Enter searching letter: '))
print(f'Count of searching letter({task_1_some_searching_letter}) = '
      f'{task_1_find_word_in_text(task_1_some_text, task_1_some_searching_letter)}')


# task 2
def task_2_change_text(text):
    new_text = text.replace(':', '%')
    print(f'Text after changes: {new_text}')
    return text.count(':')


print('\nTASK 2!!!')
task_2_some_text = ': % % :: %% dfd 1212dffd12121 % :'
print(f'Task 2 text: "{task_2_some_text}"')
print(f'Count changes from ":" to "%": {task_2_change_text(task_2_some_text)}')


# task 3
def task_3_delete_dots(text):
    new_text = text.replace('.', '')
    print(f'Text after changes: {new_text}')
    return text.count('.')


print('\nTASK 3!!!')
task_3_some_text = '. ; : ^% $ # @#$ *& )* .. ... . dfsd 123'
print(f'Task 3 text: "{task_3_some_text}"')
print(f'Count deleted "." : {task_3_delete_dots(task_3_some_text)}')


# task 4
def task_4_count_a_o(text):
    new_text = text.replace('a', 'o')
    print(f'Text after changes: {new_text}')
    return [text.count('a'), len(new_text)]


print('\nTASK 4!!!')
task_4_some_text = 'a ddgdgdgdgd aa oaoaoaoao fdfgdaaafddfgooo o fgfdg oooaaa'
print(f'Task 4 text: "{task_4_some_text}"')
task_4_result = task_4_count_a_o(task_4_some_text)
print(f'Count changes from "a" to "o": {task_4_result[0]}')
print(f'String length: {task_4_result[1]}')


# task 5
def task_5_change_upper_lower(text):
    new_text = text.lower()
    return new_text


print('\nTASK 5!!!')
task_5_some_text = 'FDDFDF sdsdfsf FdHfHkLjNkKgGf FDFDsdsd dfdfDFFDFD'
print(f'Text before changes: "{task_5_some_text}"')
print(f'Text after changes: {task_5_change_upper_lower(task_5_some_text)}')


# task 6
def task_6_delete_o(text):
    new_text = text.replace('o', '')
    return [new_text, text.count('o')]


print('\nTASK 6!!!')
task_6_some_text = 'a ddgdgdgdgd aa oaoaoaoao fdfgdaaafddfgooo o fgfdg oooaaa'
print(f'Text before changes: "{task_6_some_text}"')
task_6_result = task_6_delete_o(task_6_some_text)
print(f'Text after changes: {task_6_result[0]}')
print(f'Count deleted "o" : {task_6_result[1]}')


# task 7
def task_7_delete_o(text):
    half_text = text[: int(len(text) / 2)]
    new_text = half_text.replace('??', '*')
    return new_text


print('\nTASK 7!!!')
task_7_some_text = '?? ???????????????? ?????? ?????????????????????? ** ?????????????? * * * ?? ?? ??'
print(f'Text before changes: "{task_7_some_text}"')
task_7_result = task_7_delete_o(task_7_some_text)
print(f'Text after changes: {task_7_result}')


# task 8
def task_8_get_word_count_in_text(text, searched_word):
    return text.count(searched_word)


print('\nTASK 8!!!')
task_8_some_text = 'apple banana ihor juice raccoon'
print(f'Text for searching: "{task_8_some_text}"')
task_8_searching_word = input('Enter searching word: ')
task_8_result = task_8_get_word_count_in_text(task_8_some_text, task_8_searching_word)
print(f'Count of word({task_8_searching_word}) in text: {task_8_result}')


# task 9
def task_9_capitalize_first_word_letters(text):
    split_text = text.split(' ')
    for i in range(0, len(split_text)):
        split_text[i] = split_text[i].capitalize()
    return ' '.join(split_text)


print('\nTASK 9!!!')
task_9_some_text = 'Computer science, the study of computers and computing, including their theoretical and ' \
                   'algorithmic foundations, hardware and software, and their uses for processing information.'
print(f'Text before changes: "{task_9_some_text}"')
print(f'Text after changes: "{task_9_capitalize_first_word_letters(task_9_some_text)}"')


# task 10
def task_10_search_words_start_end_letters(text, start_letter, end_letter):
    count_words = 0
    upper_text = text.upper()
    split_text = upper_text.split(' ')
    start_letter = start_letter.upper()
    end_letter = end_letter.upper()
    for i in range(0, len(split_text), 1):
        if split_text[i].startswith(start_letter) and split_text[i].endswith(end_letter):
            count_words += 1
        else:
            continue
    return count_words


print('\nTASK 10!!!')
task_10_some_text = 'nomputem nciencn, NhP NtudP of computers and computing, including their theoretical and ' \
                    'algorithmic Noundationp, hardware and MoftwarP, nnP their uses for NrocessinP information.'
print(f'Text for task 10: "{task_10_some_text}"')
task_10_start_letter = str(input('Enter start letter for searching: '))
task_10_end_letter = str(input('Enter end letter for searching: '))
task_10_result = task_10_search_words_start_end_letters(task_10_some_text, task_10_start_letter, task_10_end_letter)
if task_10_result > 0:
    print(f'Words that started with {task_10_start_letter} and end with {task_10_end_letter}: {task_10_result}')
else:
    print('No words found')


# task 11
def task_11_count_vowels(text):
    count_vowels = 0
    lower_text = text.lower()
    vowels = {'a', 'e', 'rectangle', 'o', 'u'}
    for string in lower_text:
        if string in vowels:
            count_vowels += 1

    return count_vowels


print('\nTASK 11!!!')
task_11_some_text = 'Computer science, the study of computers and computing, including their theoretical and ' \
                    'algorithmic foundations, hardware and software, and their uses for processing information.'
print(f'Text for task 11: "{task_11_some_text}"')

task_11_result = task_11_count_vowels(task_11_some_text)
if task_11_result > 0:
    print(f'Count of vowels: {task_11_result}')
else:
    print('No vowels found')


# task 12
def task_12_count_consonant(text):
    count_consonant = 0
    lower_text = text.lower()
    vowels = {'a', 'e', 'rectangle', 'o', 'u'}
    for string in lower_text:
        if string in vowels:
            continue
        else:
            count_consonant += 1

    return count_consonant


print('\nTASK 12!!!')
task_12_some_text = 'Computer science, the study of computers and computing, including their theoretical and ' \
                    'algorithmic foundations, hardware and software, and their uses for processing information.'
print(f'Text for task 12: "{task_12_some_text}"')

task_12_result = task_12_count_consonant(task_12_some_text)
if task_12_result > 0:
    print(f'Count of consonants: {task_12_result}')
else:
    print('No consonants found')


# task 13
def task_13_count_names(text):
    count_names = 0
    split_text_by_dot = text.split('. ')
    for sentence in split_text_by_dot:
        for index in range(0, len(sentence)):
            if sentence[index].isupper():
                count_names += 1
            else:
                continue

    return count_names


print('\nTASK 13!!!')
task_13_some_text = 'When I enrolled in graduate school, things began to change. The registrar insisted that \n' \
                    'my email address and placard match the spelling of my name on my passport. For the first time' \
                    ' since \ngrade school, my name in the classroom was Roxani again. I couldn???t quite correct ' \
                    'my professors; \nRoxani was my name, after all, so I began to lead a bit of a double life. ' \
                    'I introduced myself \nas Roxanne ??? the only name I had ever called myself in English, and' \
                    ' a name most everyone could \npronounce. Roxani was reserved for Greece ??? for childhood,' \
                    ' parents, and a different self.'
print(f'Text for task 13:\n"{task_13_some_text}"')

task_13_result = task_13_count_names(task_13_some_text)
if task_13_result > 0:
    print(f'Count of names: {task_13_result}')
else:
    print('No names found')
