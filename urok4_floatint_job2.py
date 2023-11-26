#пятизначное число
chislo5 = int(input("Введите пятизначное число: "))

edinici = chislo5 % 10
desatki = (chislo5 % 100) // 10
sotni = (chislo5 % 1000) // 100
desytkitis = (chislo5 % 100000) // 10000
tis = (chislo5 % 10000) // 1000

itog = ((desatki ** edinici) * sotni) / (tis - desytkitis)
print(itog)