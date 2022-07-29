import os, string, shutil

KEY_S = input("Название файла который вы хотите найти: ")
KEY_C = input("Скопировать файлы?(если да введите '+'): ")
def path():
    lenn = 0
    for c in string.ascii_uppercase:
        disk = c+':'
        if os.path.isdir(disk):
            for file in os.walk(disk):
                lenn += len(file)
                for i in file:
                    if KEY_S in i:
                        j = "".join(i)
                        if KEY_C == "+":
                            try:
                                os.makedirs('Desktop/Copy_file_py') 
                            except:
                                next
                            filelx = j.split('\\')[-1] # Ошибка!
                            shutil.copyfile(j, os.path.join("Desktop/Copy_file_py", filelx)) # Ошибка!
                        print(j)                
    print(f"Проверено {lenn} файлов")                        
path()

# Первая версия кода
# Решено переделать код
# Ошибка с копированием файлов
# Использовать этот код как пример для лучшего решения