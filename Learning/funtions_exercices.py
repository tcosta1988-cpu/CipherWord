# Add two numbers
# Write add_numbers(a, b) that returns their sum. Call it with 4 and 7, then print the
#  result. Expected: 11.

# def add_numbers(a, b):
#     return a + b

# a = ""
# b = ""
# a = int(input("What's the first number? "))
# b = int(input("What's the second number? "))
# print(f"The sum of {a} and {b} is: {add_numbers(a, b)}")


# Convert Celsius to Fahrenheit
# Write celsius_to_fahrenheit(celsius) that returns the converted temperature. Formula: 
# celsius * 9 / 5 + 32. Try 0; expected: 32.

# def celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32

# celsius = int(input("What's the temperature in Celsius? "))
# print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")


# Check for a winner
# Write compare_scores(player, computer) that returns "You win" if the player’s score is
#  higher, "You lose" if it’s lower, and "Draw" if they’re equal. Try a few score pairs 
# and print the returned messages.

def compare_scores(player, computer):
    if player > computer:
        return "You win"
    elif player < computer:
        return "You lose"
    else:
        return "Draw"

import random

player_score = int(input("What's your score? "))
computer_score = random.randint(0, 10)  
print(f"Computer's score is: {computer_score}")
print(compare_scores(player_score, computer_score))


# 1. Find the square
# Write square(number) that returns number multiplied by itself.
# Call it with 5 and print the result. Expected: 25.


# 2. Check if a number is even
# Write is_even(number) that returns True if the number is even, otherwise False.
# Try it with 4 and 7.

# 3. Get the bigger number
# Write get_larger(a, b) that returns the larger of two numbers.
# Try it with 8 and 3. Expected: 8.

# 4. Format a full name
# Write make_full_name(first_name, last_name) that returns both names together.
# Try it with "Ada" and "Lovelace". Expected: "Ada Lovelace".

# 5. Calculate a tip
# Write calculate_tip(bill, tip_percent) that returns the tip amount.
# Try it with a bill of 50 and a tip of 10 percent. Expected: 5.