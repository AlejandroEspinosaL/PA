def cont_ciclos(n):
    """
    cont_ciclos(3)
    return 7
    
    #Esta función cuenta la cantidad de ciclos en la función de la conjetura de Collatz un problema matemático
    #tambien conocido como 3x+1, la idea la siguiente: el numero positivo que entra en la función si es
    #par se dividira entre 2 y si es impar se multiplicara por 3 y se le suma 1, el numero resultante
    #se le aplica nuevamente esta funcion y asi hasta que llega a 1(todos llegan eventualmente ahi, de eso trata la conjetura)
    #esta funcion cuenta cuantos ciclos le toma llegar a 1
    
    #ejemplo teorico n=3(impar)n=10(par)n=5(impar)n=16(par)n=8(par)n=4(par)n=2(par)n=1(alto)
    #numero de ciclos=7
    """
    num_ciclos = 0
    while not (n==1):
        if (n % 2 ==0):
            n = n/2
        else:
            n = 3*n+1
        num_ciclos += 1
    return (num_ciclos)
