# Escribe una función que permita identificar si un numer dado es primo o no


def prime(num):
    if (
        num != 0
        and num % 2 != 0
        and num % 3 != 0
        and num % 5 != 0
        and num % 7 != 0
        and num % 11 != 0
    ):
        return True


# Se puede pmantener una variable por decir: var1 = prime(2)
var2 = prime(12)
prime(32)
prime(24)
prime(65)
