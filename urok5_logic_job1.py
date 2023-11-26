a = int(input("Введите число: "))

chet = a % 2
str1 = ''
str2 = ''
if a != 0:
    if chet == 0:
        str1  = 'четное'
    else:
        str1 = 'не четное'



if a < 0:
    str2 = 'отрицательное'
elif a == 0:
    str2 = 'нулевое'
elif a > 0:
    str2 = 'положительное'

itogstr = str2 + ' ' + str1 + ' число'
print(itogstr)