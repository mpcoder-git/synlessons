# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

class turtle:
    def __init__(self, x,y,s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
        print(self.y)

    def go_down(self):
        self.y -= self.s
        print(self.y)

    def go_left(self):
        self.x -= self.s
        print(self.x)
    
    def go_right(self):
        self.x += self.s
        print(self.x)

    def evolve(self):
        self.s += 1
        print(self.s)

    def degrade(self):
        if self.s >= 1:
            self.s -= 1
            print(self.s)
        else:
            print('Невозможно уменьшить s ')

    def count_moves(self, x2, y2):
        lr = abs(x2 - self.x)
        tf = abs(y2 - self.y)
        print('Количество ходов до цели равно: ', (lr+tf)/self.s)


Turtle1 = turtle(10,10,5)
Turtle1.go_up()
Turtle1.count_moves(20,30)