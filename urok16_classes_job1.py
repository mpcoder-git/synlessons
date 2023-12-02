# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class kassa:
    def __init__(self, money):
       self.money = money
    
    def top_up(self):
        n = float(input('Введите сумму пополнения: '))
        self.money += n
        print(self.money)

    def count_1000(self):
        ts = self.money//1000
        print('Осталось целых тысяч в кассе: ',ts)
        
    def take_away(self,x):
        if x < self.money:
            self.money -= x
        else:
            print('Недостаточно денег в кассе ')

Kassa1 = kassa(100)
Kassa1.top_up()
Kassa1.count_1000()
Kassa1.take_away(50000)
print('Осталось денег после снятия: ',Kassa1.money)

