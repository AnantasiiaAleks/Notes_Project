import Note
import user_interface as ui
import file_operation as file


def add_note():
    new_note = ui.create_note()
    list_notes = file.read_file()
    for ex_note in list_notes:
        if Note.Note.get_note_id(new_note) == Note.Note.get_note_id(ex_note):
            Note.Note.set_note_id(new_note)
    list_notes.append(new_note)
    file.write_file(list_notes, 'a')
    print('Your note saved successfully!')


def show_notes(command):
    flag = True
    list_notes = file.read_file()
    if command == 'date':
        search_date = input('Please input date dd.mm.yyyy for search: ')
    for notes in list_notes:
        if command == 'all':
            flag = False
            print(Note.Note.show_note(notes))
        if command == 'id_note':
            flag = False
            print('ID: ' + Note.Note.get_note_id(notes))
        if command == 'date':
            flag = False
            if search_date in Note.Note.get_date(notes):
                print(Note.Note.show_note(notes))
    if flag:
        print('Not found notes...')

def id_functions(command):
    show_or_not_button = input('If you forgot your ID\'s, input y: ')
    if show_or_not_button == 'y':
        show_notes('id_note')
    id_search = input('Please input ID for search: ')
    list_notes = file.read_file()
    flag = True
    for notes in list_notes:
        if id_search == Note.Note.get_note_id(notes):
            flag = False
            if command == 'edit':
                corr_note = ui.create_note()
                Note.Note.set_title(notes, corr_note.get_title())
                Note.Note.set_text(notes, corr_note.get_text())
                Note.Note.set_date(notes)
                print('Your note saved successfully!')
            if command == 'del':
                list_notes.remove(notes)
                print('Your note is deleted.')
            if command == 'show':
                print(Note.Note.show_note(notes))
    if flag:
        print('Not found notes...')
    file.write_file(list_notes, 'a')