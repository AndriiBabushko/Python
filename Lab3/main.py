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
print(f'Count changes from : to %: {task_2_change_text(task_2_some_text)}')


# task 3
def task_3_delete_dots(text):
    new_text = text.replace('.', '')
    print(f'Text after changes: {new_text}')
    return text.count('.')


print('\nTASK 3!!!')
task_3_some_text = '. ; : ^% $ # @#$ *& )* .. ... . dfsd 123'
print(f'Task 3 text: "{task_3_some_text}"')
print(f'Count changes from : to %: {task_3_delete_dots(task_3_some_text)}')
