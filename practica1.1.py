def read_number(message) -> float:
    """Solicita un número al usuario"""
    is_numeric=False    #Se declara false a is_numeric

    while not is_numeric: #es un while "negativo" va a realizar la condición mientras is_numeric sea False
        number = input(message) #El numero va a ser lo que se halla escrito por el usuario 
        is_numeric=number.isnumeric() #se cambia el valor de is_numeric a True si y solo si lo que escribió el usuario 
        #es completamente numérico, esto gracias al método .isnumeric() como devuelve un True, el while not ya no se ejecuta
        #por que ya no hay un False para ejecutarse (en is_numeric)
    
    return float(number) #regresa un número flotante

min_num = read_number('Dame un número mínimo de un rango')
max_num = read_number('Dame un número máximo de un rango')

if max_num < min_num: #Si el número max. es menor que el min, entonces devuelve que los datos son invalidos
    print('Tus datos no son validos')
else:
    iterator = min_num #Sin ocupar un bucle (que bien podrían ocuparlo xd con range()) se crea un iterador 
    result = [] #Se crea una lista vacía para llenarla con los números
    while iterator <= max_num: #mienttras iterador (num_min sea menor o igual max_num) entonces agregale 1 (crear los números del rango)
        if iterator  % 3 == 0: #si el iterador es divisible entre 3 y el resultado tiene reisudo 0 entonces
            result.append(iterator) #Añade ese elemento que fue dividido como un elemento de la lista
        iterator+=1 #se pone hasta el final el +1 por que mienttras se genera se debe hacer la operación 
        #Si se hace antes no resulta por que primero va a imprimir los números xd

print('El resultado es', result) #Muestra los elementos que fueron mandados a la lista