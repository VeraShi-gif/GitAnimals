from ClassZOO import *

#Определение вида
wofl_kind = Kind("Волк", "Волчий", 10, "мясо", "да", "у-уу-у")

#Животные
wolf1 = Animal("Жора", 2, 4, wofl_kind)
wolf2 = Animal("Волчок", 3, 3, wofl_kind)

#Объявление вальера
vlr1 = Valuer("Вольер 1", "Волчий", 10)
vlr2 = Valuer("Вольер 2", "Волчий", 10)

#Информация о волках
wolf1.info()
wolf2.info()

# Присваиваем вольер
vlr1.setAnimal(wolf1)
vlr2.setAnimal(wolf2)

# Удаляем из вольера
#vlr1.delAnimal(wolf1)


#Информация о волках
wolf1.info()
wolf2.info()

#Звук волка 1
wolf1.getKindSound()




