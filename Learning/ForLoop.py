import random

#list_things = ["wave", "cat", "bootle"]


                #Imprimir lista em string horizonal
string = "Tiago Costa"
result= ""
for letter in string:
    print(letter)
    result += letter
print(result)

                #Tabuada
# num = int(input("Which number multiplication table do you want: "))
# for x in range(1, 11):
#     mult = x * num
#     print(f"{num} x {x} = {mult}")

                #Contador de Letras
# user_word = input("Enter one word: ").lower()
# size_user_word = len(user_word)
# num_letters = ""
# for letter in range(1, size_user_word + 1):
#     num_letters = letter
# print(f"You word have {num_letters} letters.")

                #Contagem
# result = ""
# for num in range(1, 11):
#     if num > 1:
#         result += "-"
#     result += str(num)
# print (result)
#

                #Correct Number, with attempts
# print("I will choose a random number (0 - 10)\nTry guess witch one I choose")
# pc_number = int(random.randint(1, 10))
# print(pc_number)
# #choose_number = int(input(f"Witch one do you think i choose? "))
# for attempt in range(1, 6):
#     choose_number = int(input(f"Witch one do you think i choose? {attempt}/5 attempt: "))
#     if choose_number > pc_number:
#         print("The number is smaller")
#     elif choose_number < pc_number:
#         print("The number is bigger")
#     elif choose_number == pc_number:
#          print("You Win!")
#          break
# else:
#     print("No more attempts\nYou Lose!")


            # Lists and For loop
# wine_list = ["Labet", "Murmures", "Overnoy", "Houillon", "Boulanger"]
# vintage = [2019, 2020, 2016, 2018, 2022]
# prices = [70, 200, 300, 120, 100]
#
# #Saber index de cada produtor (e numerate())
# for producers in enumerate(wine_list):
#     print(producers)
#
# for i, producers in enumerate(wine_list, start = 1):    # Start =1 para o index começar em 1 e nao em 0
#     #print(i)
#     #print(producers)
#     print(i, "-", producers)                            # +1 para a lsita começar no index 1 e nao no 0
#
# # agregar 2 listas numa so ( zip() )
# for wines in zip(wine_list, vintage):
#     print(wines)
#
# for wines, vintages in zip(wine_list, vintage):
#     print(wines, "-", vintages)
#
# for wines, vintages, price in zip(wine_list, vintage, prices):
#     #print(wines, "-", vintages, "-", price)
#     print(f"{wines}, {vintages}, {price}€")