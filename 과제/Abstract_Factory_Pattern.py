class Button:
    def click(self):
        pass

class DarkButton(Button):
    def click(self):
        print("dark click")

class LightButton(Button):
    def click(self):
        print("ligh click")

class CheckBox:
    def check(self):
        pass

class DarkCheckBox(CheckBox):
    def check(self):
        print("dark check")

class LightCheckBox(CheckBox):
    def check(self):
        print("light check")

class ScrollBar:
    def scroll(self):
        pass

class DarkScrollBar(ScrollBar):
    def scroll(self):
        print("dark ScrollBar")

class LightScrollBar(ScrollBar):
    def scroll(self):
        print("light ScrollBar")



class UIFactory:
    def getButton(self):
        pass
    
    def getCheck(self):
        pass
    
    def getScroll(self):
        pass

class DarkFactory(UIFactory):

    def getButton(self):
        return DarkButton()
    
    def getCheck(self):
        return DarkCheckBox()
    
    def getScroll(self):
        return DarkScrollBar()
    
class LightFactory(UIFactory):
    def getButton(self):
        return LightButton()
    
    def getCheck(self):
        return LightCheckBox()
    
    def getScroll(self):
        return LightScrollBar()
    

df = DarkFactory()
bt = df.getButton()
ck = df.getCheck()
sc = df.getScroll()
bt.click()
ck.check()
sc.scroll()