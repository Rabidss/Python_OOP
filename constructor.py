class Hero: #template #class variable

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("Sniper", 10, 50, 8)
hero2 = Hero("Mirana", 100, 80, 20)
hero3 = Hero("Sven", 1000, 70, 0)

print(hero1.__dict__)

