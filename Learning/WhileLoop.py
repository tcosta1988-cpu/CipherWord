pin_correcto = 1111
tentativas = 0

while tentativas < 3:
    pin = int(input("Introduzir PIN "))
    tentativas += 1

    if pin_correcto == pin:
        print("PIN Correcto")
        break
    else:
        print("PIN Incorreto")
        break
else:
    print("Cartao Bloqueado")