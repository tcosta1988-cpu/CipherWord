                 # Creating a dictionary
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

                    # Retrieving a value from a dictionary
# print(programming_dictionary["Function"])


                     # Adding more items to a dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."


                     # Creating an empty dictionary
# empty_dictionary = {}


                     # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)


                    # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# # print(programming_dictionary)
#

                    # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


                    # Student Grades Exerc (day 9)
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# # Classificar cada aluno
# student_grades = {}
#         # Loop through each key in the student_scores dictionary
# for student in student_scores:
#             # Get the value (student score) by using the key each time.
#     score = student_scores[student]
#             # Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#             student_grades[student] = 'Outstanding'
#     elif score >= 81:
#             student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'
#
# print(student_grades)

#Students with above > 80
# for key, value in student_scores.items():
#     if value > 80:
#         print(f"{key}: {value}", "(more than 80)")
#
# for key, value in student_scores.items():
#     print(value)


                # Wine Cellar
wine_list ={
    "Labet - Savagnin 2019": 100,
    "Boulanget - Phenomaynal 2022": 120,
    "Overnoy - Savagnin 2016": 350,
}

# lista_por_preço = []
# mais_caro = 0
# mais_barato = 999999999
# produtor = ""           #key
# preço = ""              #value
#
# produtor = str(input("Qual o Produtor - Cuvee (Ano) que quer adicionar? "))             #adicionar vinho
# valor = float(input("Qual o preço? "))                                                  #Adicionar Preço
# wine_list[produtor] = valor

# for key, value in wine_list.items():                                                   #Vinho mais caro
#     if value > mais_caro:
#         mais_caro = value
#         prod_caro = key
# print(f"o vinho mais caro é {prod_caro} com o valor de {mais_caro}€")

# for key, value in wine_list.items():                                                  #Vinho mais barto
#     if value < mais_barato:
#         mais_barato = value
#         prod_barato = key
# print(f"o vinho mais barato é {prod_barato} com o valor de {mais_barato}€")




# wine_alfabet= dict(sorted(wine_list.items()))           #organizar dicionario alfabeticamente
# print(wine_alfabet)
#
# value_mais_alto = max(wine_list.values())               #organizar por maior value
# print(value_mais_alto)


                #Dicionarios Paises : Capitais
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

                    # Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# # print(nested_list[2][1])
#
                        # Nested dictionary in a dictionary
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"],
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#    },
# }
# print(travel_log["Germany"]["cities_visited"][2])

                    # Trainning Dicionaries methods
# world_waves = {"Portugal" : ["Cova do Vapor", "Crazy Left", "Reef", "Boss", "Molhe Leste"],
#                 "Indonesia" : ["The Peak", "Leftovers", "Watukarung", "PerfectLeft"],
#                  }
# world_waves ["Espanha"] = "Andrin", "Mundaka"

# print(world_waves.items())
# print(world_waves.values())
# print(world_waves.keys())

                #listas de Contactos
# lista_contactos = {
#     "Tiago": "tiagocosta€gmail.com",
#     "Ines": "inesdias@gmail.com",
#     "cenas": "cenas@gmail.com",
#     "anonimo": "anonymous€hotmail.com"
#                 }
#
# print(lista_contactos.keys())                                                     #imprime todas as keys, em lista
# print(lista_contactos.values())                                                   #impreme todas as values , em lista
# lista_contactos["Benardo"] = "grandapalerma@facebook.com"                         #Adicionar na lista
# print(lista_contactos.items())

                         # Verificar se um contacto esta na lista. Procurar pela key
# for nome in lista_contactos:
#     if nome == "Tiago":
#         print(f"{nome} está na lista!")

# for key, value in lista_contactos.items():
#     if value == "tiagocosta€gmail.com":
#         print(value, "->", key)

