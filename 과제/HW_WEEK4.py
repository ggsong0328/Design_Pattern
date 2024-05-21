# #LAB 1
import copy
import random

# class Character:
#     @staticmethod
#     def generate_unique_id():
#         new_id = random.randint(1, 100)
#         while new_id in Character.generated_ids:
#             new_id = random.randint(1, 100)
#         Character.generated_ids.add(new_id)
#         return new_id

#     generated_ids = set()

#     def __init__(self):
#         self.health = 500
#         self.defense = 100
#         self.mana = 500
#         self.magic = 100
#         self.agility = 100
#         self.range = 100
#         self.skill = None
#         self.name = None
#         self.ID = self.generate_unique_id()

#     def clone(self):
#         cloned = copy.deepcopy(self)
#         cloned.ID = self.generate_unique_id()
#         return cloned 

# class Warrior(Character):
#     def __init__(self):
#         super().__init__()
#         self.health = 1000
#         self.defense = 500
#         self.skill = "검 스윙"

# class Wizard(Character):
#     def __init__(self):
#         super().__init__()
#         self.mana = 1000
#         self.magic = 500
#         self.skill = "파이어 볼"

# class Archer(Character):
#     def __init__(self):
#         super().__init__()
#         self.agility = 500
#         self.range = 300
#         self.skill = "정밀 사격"
        
# warrior = Warrior()
# warrior_1 = warrior.clone()
# warrior_1.name = "나는전사"
# warrior_1.agility = 50
# warrior_2 = warrior.clone()
# warrior_2.name = "나도전사"

# wizard = Wizard()
# wizard_1 = wizard.clone()
# wizard_1.name = "나는 마법사"
# wizard_1.health = 550
# wizard_2 = wizard.clone()
# wizard_2.name = "나도 마법사"

# archer = Archer()
# archer_1 = archer.clone()
# archer_1.name = "나는 궁수"
# archer_1.mana = 50
# archer_2 = archer.clone()
# archer_2.name = "나도 궁수"

# print("warrior 1 ", warrior_1.__dict__)
# print("warrior 2 ", warrior_2.__dict__)
# print("wizard 1 ", wizard_1.__dict__)
# print("wizard 2 ", wizard_2.__dict__)
# print("archer 1 ", archer_1.__dict__)
# print("archer 2 ", archer_2.__dict__)

# #LAB 2

class Character:
    def __init__(self):
        self.ID = None
        self.name = None
        self.health = 500
        self.defense = 100
        self.mana = 500
        self.magic = 100
        self.agility = 100
        self.range = 100
        self.skill = None

class CharacterBuilder:
    def __init__(self):
        self.character = Character()

    def set_name(self, name):
        self.character.name = name
        return self

    def set_health(self, health):
        self.character.health = health
        return self

    def set_defense(self, defense):
        self.character.defense = defense
        return self

    def set_mana(self, mana):
        self.character.mana = mana
        return self

    def set_magic(self, magic):
        self.character.magic = magic
        return self

    def set_agility(self, agility):
        self.character.agility = agility
        return self

    def set_range(self, range):
        self.character.range = range
        return self

    def set_skill(self, skill):
        self.character.skill = skill
        return self

    def generate_ID(self):
        self.character.ID = random.randint(1, 100)
        return self

    def build(self):
        if not self.character.name:
            raise ValueError("Name must be set")
        if not self.character.ID:
            self.generate_ID()
        return self.character

class WarriorBuilder(CharacterBuilder):
    def __init__(self):
        super().__init__()
        self.character.skill = "검 스윙"
        self.character.health = 1000
        self.character.defense = 500

class WizardBuilder(CharacterBuilder):
    def __init__(self):
        super().__init__()
        self.character.skill = "파이어볼"
        self.character.mana = 1000
        self.character.magic = 500

class ArcherBuilder(CharacterBuilder):
    def __init__(self):
        super().__init__()
        self.character.skill = "정밀 사격"
        self.character.agility = 500
        self.character.range = 300

warrior_builder = WarriorBuilder()
warrior_1 = warrior_builder.set_name("나는 전사").build()
warrior_builder_2 = WarriorBuilder()
warrior_2 = warrior_builder_2.set_name("나도 전사").build()

wizard_builder = WizardBuilder()
wizard_1 = wizard_builder.set_name("나는 마법사").build()
wizard_builder_2 = WizardBuilder()
wizard_2 = wizard_builder_2.set_name("나도 마법사").build()

archer_builder = ArcherBuilder()
archer_1 = archer_builder.set_name("나는 궁수").build()
archer_builder_2 = ArcherBuilder()
archer_2 = archer_builder_2.set_name("나도 궁수").build()

print("warrior 1", warrior_1.__dict__)
print("warrior 2", warrior_2.__dict__)
print("wizard 1", wizard_1.__dict__)
print("wizard 2", wizard_2.__dict__)
print("archer 1", archer_1.__dict__)
print("archer 2", archer_2.__dict__)

