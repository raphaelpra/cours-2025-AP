class Rectangle:
    def __init__(self, width, length):
        print("Hello, je vais creer mon rectangle", width, length)
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)

class Carre(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
    
    def perimeter(self):
        return super().perimeter() * 2


rect = Rectangle(2,3)
print(rect.perimeter())

carre = Carre(4)
print(carre.perimeter())
