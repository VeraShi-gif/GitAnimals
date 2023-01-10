
class Kind:
    def __init__(self, kindName, biom, s, food, hunter, sound):
        self.kindName = kindName
        self.biom = biom
        self.s = s
        self.food = food
        self.hunter = hunter
        self.sound = sound

    def getSound(self):
        print(self.sound)

    def info(self):
        print("Вид: " + self.kindName)
        print("Биом: " + self.biom)
        print("Площадь: " + str(self.s))
        print("Что кушает: " + self.food)


class Animal():

    def __init__(self, name, food_eat, age, kind):
        self.name = name
        self.food_eat = food_eat
        self.age = age
        self.kind = kind
        self.valuer = ""

    def setValuer(self, valuer):
        self.valuer = valuer

    def delValuer(self):
        self.valuer = ""


    def info(self):
        self.kind.info()
        print("Имя: " + str(self.name))
        print("Съел: " + str(self.food_eat))
        if self.valuer != '':
            print("Вольер: " + self.valuer.name)
        else:
            print("Вольер не определен")
        print()

    def getKindSound(self):
        print(self.kind.sound)

class Valuer():
    def __init__(self, name, biom, s):
        self.name = name
        self.biom = biom
        self.s = s

    def setAnimal(self, animal):
        animal.setValuer(self)

    def delAnimal(self, animal):
        animal.delValuer(self)
