from primePy import primes
from math import gcd
from random import randint


def numberPrime():
    foundPrime = False
    number = None
    while not foundPrime:
        number = randint(2, 100)
        if primes.check(number):
            foundPrime = True
    return number


def getE(FideN):
    numberRandom = randint(2, 100)
    while gcd(numberRandom, FideN) != 1 and numberRandom < FideN:
        numberRandom = randint(2, 100)
    return numberRandom


def euclidesExtend(entire, modulo_number):
    modulo_zero = modulo_number
    variable0 = 0
    variable1 = 1
    while entire > 1:
        quotient = entire // modulo_number
        variable = modulo_number
        modulo_number = entire % modulo_number
        entire = variable
        variable = variable0
        variable0 = variable1 - quotient * variable0
        variable1 = variable

    if variable1 < 0:
        variable1 += modulo_zero

    return variable1


def h(firm):
    return firm % 25


if __name__ == '__main__':
    p = numberPrime()
    q = numberPrime()
    my_firm = 5
    print("p -> ", p)
    print("q -> ", q)
    n = p * q
    print("n -> ", n)
    fideEuler = (p - 1) * (q - 1)
    e = getE(fideEuler)
    print("keyPublic ->", e)

    d = euclidesExtend(e, fideEuler)
    print("keyPrivate ->", d)

    print("1:cifrar")
    print("2:descifrar")
    print("3:salir")

    msg = None
    while True:
        option = input("Ingrese opción:")
        if option == "1":
            e_public = int(input("Ingrese clave publica del otro usuario:"))
            n_otherUser = int(input("Ingrese N del otro usuario:"))
            msg = int(input("Ingrese Mensaje a encriptar"))
            msg_encrypted = (msg ** e_public) % n_otherUser
            print("Mensaje encriptado :", msg_encrypted)

        elif option == "2":
            msg_encrypted = int(input("Ingrese mensaje encriptado:"))
            msg = (msg_encrypted ** d) % n
            print(msg)
        elif option == "3":
            firm = (my_firm ** d) % n
            print(firm)
        elif option == "4":
            e_public = int(input("Ingrese clave publica del otro usuario:"))
            n_otherUser = int(input("Ingrese N del otro usuario:"))
            firm_encrypted = int(input("Ingrese Firma encriptado:"))
            firm_decry = (firm_encrypted ** e_public) % n_otherUser
            print(firm_decry)
        elif option == "5":
            break
        else:
            print("No es una opción valida")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
