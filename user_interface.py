import Note

MIN_LEN_TEXT = 5


def print_menu():
    print('_' * 10 + 'Menu' + '_' * 10)
    print('Press 1-7 to select any command:\n'
          '1. Create new note\n'
          '2. Open all notes\n'
          '3. Search with id\n'
          '4. Search with date\n'
          '5. Edit note\n'
          '6. Remove note\n'
          '7. Quit')


def create_note():
    title = input("Please input your title: ")
    if len(title) == 0:
        title = 'Untitled note'
    text = check_len_text(input("Please input your text: "))
    return Note.Note(title=title, text=text)


def check_len_text(text):
    while len(text) < MIN_LEN_TEXT:
        print(f'Enter at least {MIN_LEN_TEXT} characters.\n')
        text = input('Input your text: ')
    else:
        return text


def say_goodbye():
    print('Bye-bye!')
