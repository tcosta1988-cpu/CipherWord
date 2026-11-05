# def greet():
#     print("Hello")
#     print("Welcome back")
#     print("How are you?")
# greet()


#Funcions with inputs (Parameters and Arguments)
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Welcome back {name}")
# greet_with_name("Tiago")

# EXAMPLE
# def life_in_weeks(age):
#     years_remaining = 90 - age
#     weeks_remaining = years_remaining * 52
#     print(f"You have {weeks_remaining} weeks left ")
#
# life_in_weeks(12)


#Funcions with more than 1 inputs: Posicional Arguments
#
# def greet_with (name, location):
#     print(f"Hello {name}")
#     print(f"Your location is {location}")
#
# greet_with("Tiago", "Amadora")

#Keyword Arguments
def greet_with (name, location):
    print(f"Hello {name}")
    print(f"Your location is {location}")

greet_with(name = "Tiago", location = "Amadora")