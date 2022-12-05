# Описать 3 класса животных

#Животное в зоопарке описывается на основе следующих параметров:
    #Общее описание вида:
        #Название вида (Слон, Пингвин, Тигр)
        #Необходимый биом (Тропики, Тундра, Пустыня)
        #Необходимая площадь на особь (10 м^2)
        #Что кушает (Рыба, Мясо, Сено) - Один тип животного может питаться несколькими продуктами
        #Хищник или травоядное - Отдельный параметр выделен для дальнейшего удобства
        #Издаваемый звук (Ауф, Хрю, Рррр)

    #Описание конкретного животного:
        #Имя (Петя, Симба, Матильда)
        #Объем потребляемой в сутки еды (5кг, 0.3кг)
        #Возраст (5, 1, 20)

# Функционал животного (пока достаточно условно обозначить действие выводом в консоль):
 # Есть
 # Издать звук
 # Играть

class Animal:
    def __init__(self, name, foodVolume, age):
       self.name = name
       self.foodVolume = foodVolume
       self.age = age
       self.nameofkind = ("corova", "volk", "zebra")
       self.biom = ("ravnina", "les", "savana")
       self.ploshad = ("1000 м^2")
       self.foodtype = ("trava", "miaso", "listia")
       self.ispredator = (True, False)
       self.sound = ("myyy", "yyyy", "fififi")

    def eats (self):
        print(self.name, ": pokyshal")

    def dosound (self):
        print(self.name, ": making a sound")

    def play(self):
        print(self.name, ": poigraem")