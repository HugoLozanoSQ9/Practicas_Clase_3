#Solicita al usuario un número máximo y un número mínimo en ese rango de números debemos saber cuales 
#de ellos son divisibles entre 3

bandera = True
while bandera:
    num_max = int(input('podrías darme tu numero máximo?'))
    num_min = int(input('Podrías ahora darme tu numero mininmo?'))
    if num_min >= num_max:
        print('Perdona pero tus números están mal ingresados')
    else:
        bandera = False

for i in range (num_min, num_max+1):
    
    if i % 3 != 0:
        print(i)
    else:
        print(i,'numero divisible entre 3')
 