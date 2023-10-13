class Hero: #template
    #class variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat Hero dengan nama " + inputName)

hero1 = Hero("Sniper", 10, 50, 8)
print(Hero.jumlah)
hero2 = Hero("Mirana", 100, 80, 20)
print(Hero.jumlah)
hero3 = Hero("Sven", 1000, 70, 0)
print(Hero.jumlah)



