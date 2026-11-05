# Lists - list()
shopping_list = ["Shampoo", "Apple", "Cheese"]
shopping_list.sort()        #ordenar lista por ordem alfabetica
shopping_list.reverse()     #ordenar por ordem descendente
shopping_list.append("Bread")
shopping_list.remove("Cheese")

print(shopping_list)
print(shopping_list[1])

# Sets - set()  (sempre ordenado por ordem alfabetica, sem repetiçoes)
names_set = {"Tiago", "Filipe", "Dores", "Costa"}
names_set.remove("Dores")
names_set.add("Tiago")
print(names_set)

# Tuple - tuple()   (nao se pode adicionar nem remover dados. So ler dados)
cenas_tuple = (1, 2, 3, "Agua", "Waves")
print(cenas_tuple[4])
print(cenas_tuple[2:5])
print(cenas_tuple)
print(cenas_tuple[4])