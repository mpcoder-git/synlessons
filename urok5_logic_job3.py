x = int(input("Введите минимальную инвестиционную сумму: "))
a = int(input("Введите инвестиционную сумму Майкла: "))
b = int(input("Введите инвестиционную сумму Ивана: "))

count = '0'

if a < x and b < x and (a+b)<x:
    count = '0'
elif a < x and b < x and (a+b)>x:
    count  = '1'
elif a > x and b > x and (a+b)>x:
    count  = '2'
elif a > x and b < x and (a+b)>x:
    count = 'Mike'
elif a < x and b > x and (a+b)>x:
    count = 'Ivan'

print(count);