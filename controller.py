import user_interface as ui


def run():
    # with open('notes.csv', 'a', encoding='UTF-8'):
    #     pass
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
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                ui.say_goodbye()
