import file_operations
import datetime


def delete_note(number):
    lst = []
    lines = 0
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            if len(line) > 1:
                lst.append(line.split(';'))
                lines += 1
        del lst[int(number) - 1]
        with open('data_file.csv', 'wb'):
            pass
        for i in range(lines - 1):
            file_operations.write_file(lst[i][1], lst[i][2], i + 1, lst[i][3])


def change_note(number_of_line):
    lst = []
    lines = 0
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            lst.append(line.split(';'))
            lines += 1
        title = input('Введите заголовок новой заметки: ')
        text = input('Введите содержимое: ')
        position = lst[int(number_of_line) - 1][0]
        date = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S")
        lst[int(number_of_line) - 1][3] = date
        lst[int(number_of_line) - 1] = [position, title, text, date]
        with open('data_file.csv', 'wb'):
            pass
        for i in range(lines):
            file_operations.write_file(lst[i][1], lst[i][2], lst[i][0], lst[i][3])


def show_one_note(number):
    lst = []
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            lst.append(line.split(';'))
        print(''.join(lst[number - 1]))


def search_note(date):
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            if date in line:
                print(line)


def check_file():
    lst = []
    lines = 0
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            lst.append(line.split(';'))
            lines += 1
    if len(lst) == 0:
        return 1
    else:
        return int(lst[-1][0]) + 1


def file_is_empty():
    file_list = []
    with open('data_file.csv', 'r') as csv_file:
        for line in csv_file:
            file_list.append(line)
    if len(file_list) >= 1:
        return False
    return True