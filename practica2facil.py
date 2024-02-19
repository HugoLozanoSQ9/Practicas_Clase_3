def numax(numeros):
    return max(numeros)

bandera = True

lista=[]

while bandera:
    lista.append(int(input('Podrías por favor indicarme el número que deseas agregar a la lista?')))
    continuar  =input('Deseas agregar más números? oprime la tecla "n" para detenerte')
    if continuar in ['n','N']:
        bandera = False

print('El numero más grande de los que me diste es: ',numax(lista))