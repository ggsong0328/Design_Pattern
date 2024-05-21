# Lab 1)

class Button:
    def click(self):
        pass
    
class DarkButton(Button):
    def click(self):
        print("dark click")
        
class LightButton(Button):
    def click(self):
        print("light click")
        
class RedButton(Button):
    def click(self):
        print("red click")

class BlueButton(Button):
    def click(self):
        print("blue click")

class ScrollBar:
    def scroll(self):
        pass
    
class DarkScrollBar(ScrollBar):
    def scroll(self):
        pass
    
class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light ScrollBar")
        
class RedScrollBar(ScrollBar):
    def scroll(self):
        print("red ScrollBar")
        
class BlueScrollBar(ScrollBar):
    def scroll(self):
        print("blue ScrollBar")
        
class CheckBox:
    def check(self):
        pass
    
class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")
        
class LightCheckBox(CheckBox):
    def check(self):
        print("light check")
        
class RedCheckBox(CheckBox):
    def check(self):
        print("red check")
        
class BlueCheckBox(CheckBox):
    def check(self):
        print("blue check")

class Slider:
    def slide(self):
        pass
    
class DarkSlider(Slider):
    def slide(self):
        print("dark slide")
        
class LightSlider(Slider):
    def slide(self):
        print("light slide")
        
class RedSlider(Slider):
    def slide(self):
        print("red slide")
    
class BlueSlider(Slider):
    def slide(self):
        print("blue slide")
        
class TextBox:
    def text(self):
        pass
    
class DarkTextBox(TextBox):
    def text(self):
        print("dark text")
        
class LightTextBox(TextBox):
    def text(self):
        print("light text")
        
class RedTextBox(TextBox):
    def text(self):
        print("red text")
        
class BlueTextBox(TextBox):
    def text(self):
        print("blue text")
        
        
class UIFactory:
    def getButton(self):
        pass
    def getScroll(self):
        pass
    def getCheck(self):
        pass
    def getSlider(self):
        pass
    def getTextBox(self):
        pass
    
class DarkFactory(UIFactory):
    def getButton(self):
        return DarkButton()
    
    def getScroll(self):
        return DarkScrollBar()
    
    def getCheck(self):
        return DarkCheckBox()
    
    def getSlider(self):
        return DarkSlider()
    
    def getTextBox(self):
        return DarkTextBox()
    
class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()
    
    def getScroll(self):
        return LightScrollBar()
    
    def getCheck(self):
        return LightCheckBox()
    
    def getSlider(self):
        return LightSlider()
    
    def getTextBox(self):
        return LightTextBox()
    
class RedFactory(UIFactory):
    def getButton(self):
        return RedButton()
    
    def getScroll(self):
        return RedScrollBar()
    
    def getCheck(self):
        return RedCheckBox()
    
    def getSlider(self):
        return RedSlider()
    
    def getTextBox(self):
        return RedTextBox()
    
class BlueFactory(UIFactory):
    def getButton(self):
        return BlueButton()
    
    def getScroll(self):
        return BlueScrollBar()
    
    def getCheck(self):
        return BlueCheckBox()
    
    def getSlider(self):
        return BlueSlider()
    
    def getTextBox(self):
        return BlueTextBox()
    
    
# Lab 2)

class Shape:
    def draw(self):
        pass
        
class Factory:
    def create_shape(self) -> Shape:
        pass
    
class Circle(Shape):    
    def draw(self):
        print("Drawing a circle")
        
class Square(Shape):
    def draw(self):
        print("Drawing a square")
        
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")
        
class CircleFactory(Factory):
    def __init__(self):
        self.count = 0
    
    def create_shape(self) -> Shape:
        self.count += 1
        return Circle()
    
class SquareFactory(Factory):
    def create_shape(self) -> Shape:
        return Square()
    
    def rotate(self):
        print("Square Rotated")
    
class RectangleFactory(Factory):
    def create_shape(self) -> Shape:
        return Rectangle()
    
class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")
        
class TriangleFactory(Factory):
    def create_shape(self):
        return Triangle()
    
    
class Drawing:
    def draw_shape(self, shape):
        shape.draw()