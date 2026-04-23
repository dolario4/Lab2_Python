class Figure:
    def __init__ (self, name):
        self.name = name
    def area_comparison(self, other):
        if self.area() > other.area():
            return f"Площадь {self.name} больше площади {other.name}"
        elif self.area() < other.area():
            return f"Площадь {self.name} меньше площади {other.name}"
        else:
            return f"Площади {self.name} и {other.name} равны"
    def perimeter_comparison(self, other):
        if self.perimeter() > other.perimeter():
            return f"Периметр {self.name} больше периметра {other.name}"
        elif self.perimeter() < other.perimeter():
            return f"Периметр {self.name} меньше периметра {other.name}"
        else: return f"Периметры {self.name} и {other.name} равны"
        
class Square(Figure):
    def __init__ (self, name, side_length):
        super().__init__(name)
        self.side_length = side_length
    def area(self):        return self.side_length ** 2
    def perimeter(self):        return self.side_length * 4

class Rectangle(Figure):
    def __init__ (self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    def area(self): return self.width * self.height
    def perimeter(self): return 2*(self.width + self.height)

class Circle(Figure):
    def __init__ (self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self): return 3.14 * self.radius ** 2
    def perimeter(self): return 2* 3.14 * self.radius

class Triangle(Figure):
    def __init__(self, name, height, base):
        super().__init__(name)
        self.height = height
        self.base = base
    def area(self): return 0.5 * self.base * self.height
    def perimeter (self): return 3 * self.base

kvadrat = Square("Квадрат", 5)
pryamougolnik = Rectangle("Прямоугольник", 4, 6)
krug = Circle("Круг", 3)
treugolnik = Triangle("Треугольник", 4, 5)
print(f"Площадь фигур:\n{kvadrat.name} : {kvadrat.area()}\n{pryamougolnik.name} : {pryamougolnik.area()}\n{krug.name} : {krug.area()}\n{treugolnik.name} : {treugolnik.area()}")
print(f"Периметр фигур:\n{kvadrat.name} : {kvadrat.perimeter()}\n{pryamougolnik.name} : {pryamougolnik.perimeter()}\n{krug.name} : {krug.perimeter()}\n{treugolnik.name} : {treugolnik.perimeter()}")
print(kvadrat.area_comparison(pryamougolnik))
print(kvadrat.perimeter_comparison(pryamougolnik))
print(krug.area_comparison(treugolnik))
print(krug.perimeter_comparison(treugolnik))
