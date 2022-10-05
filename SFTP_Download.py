import pysftp
import os
import datetime

exp1 = False

# defining the host, username, and password
my_Hostname = "***"
my_Username = "***"
my_Password = "***"
my_Port = 7477

cnOpts = pysftp.CnOpts()
cnOpts.hostkeys = None

path = input("Введите полный путь: ")
if path == '':
    print('Путь не указан.')
    quit()

conn = pysftp.Connection(host=my_Hostname, username=my_Username, port=my_Port, cnopts=cnOpts, password=my_Password)
with conn as sftp:
    print("Успешное соединение ... ")

    with conn.cd('mods'):
        files = conn.listdir()
        start_download_time = datetime.datetime.now()
        print('Время начала загрузки: ', start_download_time)
        try:
            for file in files:
                if not os.path.exists(path + '/' + file) and (file[-4:] == '.jar'):
                    conn.get(file, os.path.join(path, file))
                    print(file, ' успешно загружен! ')
        except Exception:
            print('Произошла ошибка! Запустите программу повторно.')
            exp1 = True
        if not exp1:
            print('Все нужные файлы установлены!')
        end_download_time = datetime.datetime.now() - start_download_time
        print('Прошло:', end_download_time)
