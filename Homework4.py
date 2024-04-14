immutable_var = 11, True, "Hello", 2.5
print(immutable_var)
immutable_var [1] = False  #Изменить элементы нельзя, т.к. кортеж не поддерживает обращение по элементам(неизменяемая упорядоченная коллекция)
mutable_list = [12, False, "Python", 3.7]
mutable_list[0] = 23
mutable_list[1] = True
mutable_list[2] = "Cobra"
mutable_list[3] = 4.5
print(mutable_list)
