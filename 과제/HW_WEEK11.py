from typing import List

class Handler:
    def __init__(self):
        self.next_handler = None
    def setNext(self, handler):
        self.next_handler = handler
    def handle(self,req):
        if self.next_handler:
            return self.next_handler.handle(req)
        print("All hanlder failed")
        return None

class CashHandler(Handler):
    def handle(self,req):
        if req['method']== 'cash':
            print(f"processing cash {req['amount']} won")
        else:
            print(f"CashHandler cannot process")
            super().handle(req)
            
class CreditCardHandler(Handler):
    def handle(self,req):
        if req['method']== 'creditCard':
            print(f"processing creditCard {req['amount']} won")
        else:
            print(f"CreditCardHandler cannot process")
            super().handle(req)
            
class DebitCardHandler(Handler):
    def handle(self,req):
        if req['method']== 'debitCard':
            print(f"processing debitCard {req['amount']} won")
        else:
            print(f"DebitCardHandler cannot process")
            super().handle(req)

class PaypalHandler(Handler):
    def handle(self,req):
        if req['method']== 'paypal':
            print(f"processing paypal {req['amount']} won")
        else:
            print(f"PaypalHandler cannot process")
            super().handle(req)
            
class BitcoinHandler(Handler):
    def handle(self,req):
        if req['method']== 'bitcoin':
            print(f"processing bitcoin {req['amount']} won")
        else:
            print(f"BitcoinHandler cannot process")
            super().handle(req)

cash_handler = CashHandler()
creditcard_handler = CreditCardHandler()
debitcard_handler = DebitCardHandler()
paypal_handler = PaypalHandler()
bitcoin_handler = BitcoinHandler()

cash_handler.setNext(creditcard_handler)
creditcard_handler.setNext(debitcard_handler)
debitcard_handler.setNext(paypal_handler)
paypal_handler.setNext(bitcoin_handler)

payment = {
    "method" : "paypal",
    "amount" : 10000
}

cash_handler.handle(payment)

payment = {
    "method" : "bitcoin",
    "amount" : 10000
}

cash_handler.handle(payment)

payment = {
    "method" : "COIN",
    "amount" : 10000
}

cash_handler.handle(payment)










class Command:
    def execute(self):
        pass

class Invoker:
    def __init__(self):
        self.command_list = []

    def addCommand(self, command:Command):
        self.command_list.append(command)

    def runCommands(self):
        for command in self.command_list:
            command.execute()

class Dog:
    def sit(self):
        print("The dog sat down")
    def stay(self):
        print("The dog is staying")

class DogCommand(Command):
    def __init__(self, dog:Dog, commands:List[str]):
        self.dog = dog
        self.commands = commands
    def execute(self):
        for command in self.commands:
            if command == 'sit':
                self.dog.sit()
            elif command == 'stay':
                self.dog.stay()


class Cat:
    def jump(self):
        print("The cat jumped")
    def meow(self):
        print("The cat is meowing")

class CatCommand(Command):
    def __init__(self, cat: Cat, commands: List[str]):
        self.cat = cat
        self.commands = commands
    def execute(self):
        for command in self.commands:
            if command == 'jump':
                self.cat.jump()
            elif command == 'meow':
                self.cat.meow()


dog = Dog()
cat = Cat()

dog_command = DogCommand(dog, ['sit', 'stay'])
cat_command = CatCommand(cat, ['jump', 'meow'])

invoker = Invoker()
invoker.addCommand(dog_command)
invoker.addCommand(cat_command)

invoker.runCommands()