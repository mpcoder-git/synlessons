#гласные буквы  «a», «e», «i», «o», «u»
slovo = input("Введите слово латинскими маленькими буквами: ")
soglbukv = 0
glassnbukv = 0

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for element in slovo:
    if element == 'a' or element == 'e' or element == 'i' or element == 'o' or element == 'u': 
        glassnbukv += 1
        if element == 'a':
           count_a += 1
        if element == 'e':
            count_e += 1
        if element == 'i':
            count_i += 1
        if element == 'o':
            count_o += 1
        if element == 'u':
            count_u += 1    
    else:
        soglbukv += 1
        
    
print ('Согласных букв',soglbukv,', Гласных букв', glassnbukv)
print ('Количество букв a =',count_a,', Количество букв e =', count_e,
       'Количество букв i =',count_i,', Количество букв o =', count_o, 'Количество букв u =',count_u)

