import file_operations as fw
import datetime
import commands as c


def menu():
    number_of_line = c.check_file()
    while True:
        print('1. Показать все записи.')
        print('2. Добавить новую запись.')
        print('3. Показать одну запись')
        print('4. Удалить запись')
        print('5. Редактировать запись')
        print('6. Отсортировать заметки по дате')
        print('7. Выход из меню')
        print()

        try:
            n = int(input('Выберите пункт меню: '))
        except:
            print('Введите число!')
            continue

        if n == 1:
            if c.file_is_empty():
                print('Заметок нет')
                continue
            fw.show_file()
        elif n == 2:
            title = input('Введите название заметки: ')
            text = input('Введите текст: ')
            date = datetime.datetime.today().strftime("%d.%m.%Y %H.%M.%S")
            fw.write_file(title, text, number_of_line, date)
            number_of_line += 1
        elif n == 3:
            if c.file_is_empty():
                print('Заметок нет')
                continue
            fw.show_file()
            position = int(input('Введите порядковый номер заметки: '))
            try:
                c.show_one_note(position)
            except:
                print('Нет такой заметки')
        elif n == 4:
            if c.file_is_empty():
                print('Заметок нет')
                continue
            fw.show_file()
            num = input('Введите номер заметки: ')
            try:
                c.delete_note(num)
                number_of_line -= 1
            except:
                print('Неверный ввод')
        elif n == 5:
            if c.file_is_empty():
                print('Заметок нет')
                continue
            fw.show_file()
            num = input('Введите номер заметки: ')
            if int(num) <= number_of_line:
                c.change_note(num)
            else:
                print('Такого номера нет')
        elif n == 6:
            if c.file_is_empty():
                print('Заметок нет')
                continue
            date = input('Введите дату в формате dd.mm.yyyy: ')
            c.search_note(date)
        elif n == 7:
            break
        else:
            print('Неверная команда')