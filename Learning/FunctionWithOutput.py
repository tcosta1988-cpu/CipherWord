# def format_name(f_name, l_name):
#     #print(f_name.title())
#     #print(l_name.title())
#     if f_name == "" or l_name == "":
#         return "Invalid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     #print(f"{formated_f_name} {formated_l_name}")
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name(input("Your first name: "), input("Your last name: ")))


                    #Exercicio Day10 (Ano bisexto, True or False

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
#
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

year = (int(input("Insert year\n")))
while True:
    if True:
        print(f"The {year} its Leap")
        break
    else:
        print(f"The {year} its Not Leap")
        break