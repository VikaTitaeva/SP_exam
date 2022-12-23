        # второй скрипт для чтения файла
try:
    file = open('FIO.txt', 'r', encoding='utf8') #открытие файла с возможностью чтения
    print('id '+'фамилия ' + ' имя ' + ' отчество ' + ' возраст ' + '\n')
    while True:
        list = file.readline()
        if not list:
            break
        print(str(list))
except:
    print('Файл сломался, система тоже')
finally:
    file.close()