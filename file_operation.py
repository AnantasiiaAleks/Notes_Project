import Note


def write_file(array):
    with open('notes.csv', 'a', encoding='UTF-8', newline='') as file:
        for notes in array:
            file.write(Note.Note.to_string(notes))


def read_file():
    try:
        list_notes = []
        with open("notes.csv", "r", encoding='utf-8') as file:
            notes = file.read().strip().split("\n")
            for n in notes:
                split_n = n.split(';')
                note = Note.Note(
                    note_id=split_n[0], title=split_n[1], text=split_n[2], date=split_n[3])
                list_notes.append(note)
    except Exception:
        print('Not found notes...')
    finally:
        return list_notes
