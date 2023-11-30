#Задание №1
#Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)
print("Введенные числа:", numbers)
cnt = 0
for x in numbers:
    if x == 0:
        cnt += 1
print('Количество нулей равно ', cnt)