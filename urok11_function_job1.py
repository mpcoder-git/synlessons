#Задание №1
#Создайте функцию, которая принимает в качестве параметра - натуральное целое число.
#Данная функция находит факториал полученного числа
#Например, факториал числа 3 это число 6.
#Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.
#В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3) и вам нужно сделать список из факториалов числа 6 в убывающем порядке. Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так далее вплоть до 1
#То есть, результирующий список будет выглядеть в нашем примере так: 
#[720, 120, 24, 6, 2, 1]

def factorialfunc(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

m = factorialfunc(3)

spisok  = []

for x in range(m,1,-1):
    spisok.append(factorialfunc(x))

print(spisok)