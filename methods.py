class Hero:
    #class variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    #void function, method tanpa return, method tanpa argument
    def siapa(self):
        print("Name of Heroes is " + self.name)

    #method dengan argument, tanpa return
    def HealthUp(self,up):
        self.health += up

    #method dengan return
    def GetHealth(self):
        return self.health
            
hero1 = Hero("Sniper", 100, 8, 10)
hero2 = Hero("Mirana", 90, 5, 8)

hero1.siapa()
hero1.HealthUp(10)

print(hero1.GetHealth())