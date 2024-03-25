import user_interface as ui
import note_operations


def run():
    command = '-1'
    while command != '7':
        ui.print_menu()
        print()
        command = input('Enter your choice: ')

        while command not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Wrong! Try again...')
            command = input('Enter your choice: ')

        match command:
            case '1':
                note_operations.add_note()
            case '2':
                note_operations.show_notes('all')
            case '3':
                note_operations.id_functions('show')
            case '4':
                note_operations.show_notes('date')
            case '5':
                note_operations.id_functions('edit')
            case '6':
                note_operations.id_functions('del')
            case '7':
                ui.say_goodbye()
