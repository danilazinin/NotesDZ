def write_file(title, text, position, date):
    with open('data_file.csv', 'a', encoding='utf-8') as data:
        data.write('{}; {}; {}; {};\n'.format(position, title, text, date))


def show_file():
    with open('data_file.csv', 'r', encoding='utf-8') as data:
        lines = data.readlines()
        for line in lines:
            print(line)