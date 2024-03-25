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
