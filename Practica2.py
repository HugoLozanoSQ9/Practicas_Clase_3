""" 
Escibe una función que reciba varios números y enlista el mayor de ellos
"""
def mayor(*args):
    """Esta función recibe varios elementos y enlista el mayor de ellos
    """
    
    for arg in args:
        n=len(arg)
        print(arg)
        for i in range(0, n):
            for j in range(0, n-i-1):
                if arg[j] > arg[j+1]:
                    arg[j], arg[j+1] = arg[j+1], arg[j]
                    print(arg)
    mayor=arg[n-1]
    print('Tu numero mayor es:', mayor)
    return arg
    
        
    


bandera = True

lista=[]

while bandera:
    lista.append(int(input('Podrías darme los números de tu lista a ordenar? ')))  
    continuar = input('Deseas agregar algún otro número? y/n ')
    if continuar in ['n','N','no','NO']:
        bandera=False

mayor(lista)
    
    



