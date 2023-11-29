#Задание №3
#На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. 
#Одна лодка может выдержать не более m килограмм,
#при этом в лодку помещается не более 2 человек.
#Определите, какое минимальное число лодок нужно,
#чтобы перевезти на другой берег всех рыбаков
#В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса,
#которую может выдержать одна лодка.
#Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков.
#В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) -
#вес каждого путешественника.
#Программа должна вывести одно число - минимальное количество лодок,
#необходимое для переправки всех рыбаков на противоположный берег.

m = int(input("максимальная масса которую может выдержать одна лодка: "))
n = int(input("Введите количество рыбаков: "))

boats = 0
left = 0
right = n-1

if n >= 1 and n <= 100 and m >= 1 and m <= 10e6:

    numbers = []
    indexses = [] #те кто переправился
    for i in range(n):
        number = int(input("Введите вес путешественника: "))
        if number >= 1 and number <= m:
            numbers.append(number)
    
    numbers.sort()

    
    while left <= right:
        #если вес обоих допустим с грузоподъемностью
        if (left != right) and (numbers[left] + numbers[right]) <= m:           
            if left != right:
                indexses.append(numbers[left])
                indexses.append(numbers[right])
            elif left == right:
                indexses.append(numbers[left])
            boats += 1
            left += 1
            right -= 1

        elif (left == right) and numbers[left] <= m:
            indexses.append(numbers[left])
            boats += 1
            left = 100 #выходим из цикла

        #если вес больше предела
        elif (numbers[left] + numbers[right]) > m:
            if right > left:
                right -= 1    


indexses.sort()

    
#удалим из списка тех кто переправился
for i in indexses:
    numbers.remove(i)  


#остальные переправляются по одному
for i in numbers:
    boats += 1

print('Количество лодок для переправки равно ',boats)