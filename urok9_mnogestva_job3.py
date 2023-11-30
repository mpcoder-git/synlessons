#Задание №3
#Во входную строку вводится последовательность чисел через пробел. Для каждого числа выведите слово ”YES” (в отдельной строке), 
#если это число ранее встречалось в последовательности или ”NO”, если не встречалось.
input_string = input("Введите значения через пробел: ")
#values = input_string.split()
values = [int(x) for x in input_string.split()]
newvalues = []
print(values)

cnt = 0

for i in values:
    finded = 0
    srez = values[0:cnt]
    for y in srez:
        if y == i and cnt > 0:
            finded = 1
            newvalues.append('yes')       
    cnt += 1
    if finded == 0:
        newvalues.append('no')
 
 
print(newvalues)   
