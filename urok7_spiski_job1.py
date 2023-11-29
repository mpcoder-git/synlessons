#Задание №1
#В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.
n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    number = int(input("Введите число: "))
    if number >= 1 and number <= 10000 and abs(number) < 10e5:
        numbers.append(number)

numbers.reverse()
print(numbers)