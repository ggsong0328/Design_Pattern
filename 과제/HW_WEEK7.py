# 1번 - 6개

class TestUnit:
    def run(self):
        pass

class System:
    def __init__(self, testUnit:TestUnit):
        self.testUnit = testUnit

    def start_test(self):
        pass


class Android(System):
    def start_test(self):
        self.testUnit.run()
        print("Android")

class IOS(System):
    def start_test(self):
        self.testUnit.run()
        print("IOS")

class Dijkstra(TestUnit):
    def run(self):
        print("Dijkstra Algorithm")

class MinimumSpanningTree(TestUnit):
    def run(self):
        print("MinimumSpanningTree Algorithm")

class A_star(TestUnit):
    def run(self):
        print("A_star Alorithm")

#Client Code
android_system = Android(Dijkstra())
android_system.start_test()

ios_system = IOS(MinimumSpanningTree())
ios_system.start_test()

class CarColor:
    def __init__(self, color_name, rgb_value):
        self.color_name = color_name
        self.rgb = rgb_value

    def __str__(self):
        return self.color_name

class Car:
    _Color_Table = {}
    
    def addRGB(color, RGB):
        color_RGB = CarColor(color, RGB)
        Car._Color_Table[color] = color_RGB
    
    def __init__(self, year, brand, name, fuel_type, color):
        self.year = year
        self.brand = brand
        self.name = name
        self.fuel_type = fuel_type
        self.color = color
        if color not in Car._Color_Table:
            raise RuntimeError(f"{color} is not in Color_Table")

    def __str__(self):
        return f"{self.year} {self.brand} {self.name}, Fuel: {self.fuel_type}, Color: {self.color}"

Car.addRGB("red", (255, 0, 0))
Car.addRGB("white", (255, 255, 255))
Car.addRGB("green", (0, 255, 0))

car1 = Car("Audi", "R8", 2017, "disel", "red")
car2 = Car("Lamborghini", "Aventador", 2011, "gasoline", "green")
car3 = Car("Hyundai", "IONIQ5", 2021, "electric", "white")

print(car1)
print(car2)
print(car3)
