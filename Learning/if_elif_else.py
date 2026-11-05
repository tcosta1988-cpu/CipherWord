                    # Bigger Number
print("I´ll say you a bigger number in the next 5 ones")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a next one: "))
num3 = int(input("Enter a next one: "))
num4 = int(input("Enter a next one: "))
num5 = int(input("Enter a last one: "))

bigger_number = ""
if num1 > num2:
    print(f"Bigger number is = {num1}")
elif num2 > num3:
    print(f"Bigger number is = {num2}")
elif num3 > num4:
    print(f"Bigger number is = {num3}")
elif num4 > num5:
    print(f"Bigger number is = {num4}")
else:
    print(f"Bigger number is = {num5}")