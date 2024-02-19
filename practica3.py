#Escribir una función que permita multiplicar varios números 

def multiply(*args):

    start = 1
    for arg in args:
        start *= arg
    return start

bandera= True

lista=[]

while bandera:
    lista.append(int(input('Podrías por favor indicarme el número que deseas agregar a la lista?')))
    continuar  =input('Deseas agregar más números? oprime la tecla "n" para detenerte')
    if continuar in ['n','N']:
        bandera = False

print(multiply(*lista))