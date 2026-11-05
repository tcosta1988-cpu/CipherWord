                # Repeat with optcion str:
# repeat = "r"
# while repeat == "r":
#     repeat = input("Repetir ou Sair? R - S\n").lower()
#     if repeat == "r":
#         print("---- FAZER CENAS ----")
#     elif repeat == "s":
#         print("--- Fim---")
#

                # Repeat with optcion int:
def repeat_cycle():
    """funçao para perguntar ao utilizador se quer repetir o programa"""
    while True:
        repeat = input("Repetir ou Sair? R - S\n").lower()
        if repeat == "r":
            print("---- FAZER CENAS ----")
        elif repeat == "s":
            print("--- Fim---")
            break

