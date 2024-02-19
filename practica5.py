def isin(*args):

    number =  int(input('Podrías decirme el número que vamos a corroborar?'))

    if number in args:
        print('Es correcto tu número existe en la lista')
    else:
        print('Tu numero no se encuentra en la lista')

lista=[]

bandera = True

while bandera:
    lista.append(int(input('Podrías por favor indicarme el número que deseas agregar a la lista?')))
    continuar  =input('Deseas agregar más números? oprime la tecla "n" para detenerte')
    if continuar in ['n','N']:
        bandera = False

isin(*lista)