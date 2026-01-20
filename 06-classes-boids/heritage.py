import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    def xx(self):
        return 2

vector = Vector(2, 2)
vector.length()

print('dir', dir(vector))



class A(B,C):
    def __init__(self):
        pass


class Aprime():
    def __init__(self):
        self.b = B(self)
        self.c = C(self)

a = A()
a.ma_method_definie_sur_b()

a_prime = Aprime()
a_prime.b.ma_method_definie_sur_b()
