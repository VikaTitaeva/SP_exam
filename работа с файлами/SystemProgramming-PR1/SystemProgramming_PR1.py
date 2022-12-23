    # первый скрипт для ввода данных в файл
print ("Введите через пробел ID, фамилию, имя, отчество, возраст")
def isint(i): # функция для проверки, является ли переменная числом
    try:
        int(i)
        return True
    except ValueError:
        return False
while True:
    try:
        file = open('FIO.txt', 'a', encoding='utf8') #открытие файла с возможностью добавления записи
        try:
            id, surname, name, patronymic, old = map(str, input().split())
            if id =='-' and surname == '-' and name == '-' and patronymic == '-' and old == '-':
                break
            elif isint(old) and len(old) <=2:# проверка того, что возраст не может быть больше 100
                file.write(str(id)+' '+ str(surname) + ' ' + str(name) + ' ' + str(patronymic) + ' ' + str(old) + ' ' + '\n') # запись в файл
            else:
                print('Слишком много лет1!')
        except ValueError:
            print('Проверьте правильность введенных данных!')
        finally:
            file.close()
    except:
        print('Файл сломался, система тоже')


