class Memo:
    def __init__(self):
        self.memo_list = []
        
    def addMemo(self, memo): #메모를 리스트로 추가하는 기능
        self.memo_list.append(memo)
        
    def printMemo(self): #모든 메모를 콘솔로 출력하는 기능
        for i in range(len(self.memo_list)):
            print(f'{i + 1}. {self.memo_list[i]}')
            
    def saveMemo(self, memo): #메모를 파일에 저장하는 기능
        with open(memo, "w") as file:
            for memos in self.memo_list:
                file.write(memos + "\n")
    
    def getMemo(self, memo): #파일로부터 메모를 불러오는 기능
        with open(memo, "r") as file:
            contents = file.read()
            
class Memo:
    def __init__(self):
        self.memo_list = []
        
    def addMemo(self, memo):
        self.memo_list.append(memo)
        
    def printMemo(self):
        for i in range(len(self.memo_list)):
            print(f'{i + 1}. {self.memo_list[i]}')
            
    def saveMemo(self, file_path):
        memo_data = '\n'.join(self.memo_list)
        file_writer = FileWriter()
        file_writer.write(file_path, memo_data)
    
    def loadMemo(self, file_path):
        file_reader = FileReader()
        self.memo_list = file_reader.read(file_path)

class FileWriter:
    def write(self, file_path, data):
        with open(file_path, "w") as file:
            file.write(data)

class FileReader:
    def read(self, file_path):
        with open(file_path, "r") as file:
            return file.readlines()
        
class Employee:
    def __init__ (self, type_of_employee, base_salary):
        self. type_of_employee = type_of_employee
        self.base_salary = base_salary

    def calculate_salary(self):
        if self. type_of_employee == "permanent":
            return self.base_salary + 1000
        elif self. type_of_employee == "temporary":
            return self.base_salary + 500
        elif self. type_of_employee == "intern":
            return self.base_salary + 200

permanent_employee = Employee ("permanent", 3000)
print (permanent_employee.calculate_salary())
temporary_employee = Employee("temporary", 3000)
print (temporary_employee.calculate_salary())
intern_employee = Employee("intern", 3000)
print(intern_employee.calculate_salary())


class Employee:
    def __init__(self, type_of_employee, base_salary):
        self.type_of_employee = type_of_employee
        self.base_salary = base_salary

class SalaryCalculator:
    def calculate_salary(employee):
        base_salary = employee.base_salary
        if employee.type_of_employee == "permanent":
            return base_salary + 1000
        elif employee.type_of_employee == "temporary":
            return base_salary + 500
        elif employee.type_of_employee == "intern":
            return base_salary + 200

permanent_employee = Employee("permanent", 3000)
print(SalaryCalculator.calculate_salary(permanent_employee))

temporary_employee = Employee("temporary", 3000)
print(SalaryCalculator.calculate_salary(temporary_employee))

intern_employee = Employee("intern", 3000)
print(SalaryCalculator.calculate_salary(intern_employee))

class Light:
    def turn_on(self):
        print("Light turned on")
        
    def turn_off(self):
        print("Light turned off")
        
class Fan:
    def turn_on(self):
        print("Fan turned on")
    
    def turn_off(self):
        print("Fan turned off")
        
class Switch:
    def __init__(self):
        self.light = Light()
        self.fan = Fan()
        
    def turn_light_on(self):
        self.light.turn_on()
        
    def turn_light_off(self):
        self.light.turn_off()
        
    def turn_fan_on(self):
        self.fan.turn_on()
        
    def turn_fan_off(self):
        self.fna.turn_off()
        
        
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class Light(Switchable):
    def turn_on(self):
        print("Light turned on")
        
    def turn_off(self):
        print("Light turned off")
        
class Fan(Switchable):
    def turn_on(self):
        print("Fan turned on")
    
    def turn_off(self):
        print("Fan turned off")
        
class Switch:
    def __init__(self, device):
        self.device = device
        
    def turn_on(self):
        self.device.turn_on()
        
    def turn_off(self):
        self.device.turn_off()

