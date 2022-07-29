import os, shutil, string

try:
    os.makedirs('Desktop/Copy_file_py')
except:
    print("Файл уже существует")

KEY_FOR_SEARCH = input('(ничего не пишите если хотите найти всё)\nЧто хотите найти?: ')
KEY_FOR_TYPE = input('(txt, mp3, xml. Ничего не пишите если хотите найти всё)\nКакой тип файла хотите найти?:')

if KEY_FOR_TYPE.strip():
    KEY_FOR_TYPE = '.' + KEY_FOR_TYPE
    print(f'Вы выбрали: {KEY_FOR_TYPE.replace(KEY_FOR_TYPE[0], "", 1)}')

copyornot = input('Скопировать?(напишите "+" если да)\n')
def search():
    for c in string.ascii_uppercase:
        disk = c + ':'
        if os.path.isdir(disk):
            for adress, dirs, files in os.walk(disk):
                for file in files:
                    if KEY_FOR_SEARCH in file and "$" not in file and file.endswith(KEY_FOR_TYPE):
                        filejoin = os.path.join(adress, file)
                        print(filejoin)
                        if "+" in copyornot:
                            try:
                                file_name = filejoin.split('\\')[-1]
                                shutil.copyfile(filejoin, os.path.join('Desktop/Copy_file_py', file_name))
                                print("файл(ы) успешно скопирован(ы)", file_name)
                            except:
                                print("файл невозможно скопировать или он уже существует")
search()