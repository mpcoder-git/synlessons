#Задание №2
#Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.
stroka = "one    two      three   "

while stroka.find('  ') > 0:
    stroka  = stroka.replace('  ',' ')

print(stroka)