#Задание №2
#В первую строчку вводится число N (1 ≤ N ≤ 100 000). 
#В следующую строку через пробел вводятся N чисел (1 ≤ Ai ≤ 10e9). 
#Вам требуется написать метод, который получает на вход массив и изменяет его таким образом, чтобы на первом месте стоял последний элемент, на втором - первый, на третьем - второй и т. д. Выведите N чисел - измененный массив.
n = int(input("Введите количество чисел: "))
if n >= 1 and n <= 100000:
    numbers = []
    numbers2 = []

    for i in range(n):
        number = int(input("Введите число: "))
        if number >= 1 and number <= 10e9:
            numbers.append(number)

    print(numbers)

    for num in numbers:
        if num == n:
            numbers2.append(num)
    for num in numbers:
        if num in range(0,n):
            numbers2.append(num)
        

    print(numbers2)