def dist_l1(U, V):
    """
    >>>dist_l1([ 1 , 2, 4 ],[ 4 , 7, 10 ])
    14
    """
    dist_tax = 0
    for i in range(len(U)):
        dist_tax += abs(U[i]-V[i])
    return (dist_tax)

def dist_l2(U,V):
    """
    >>>dist_l2([ 1 , 2, 4 ],[ 4 , 7, 10 ])
    8.366600265340756
    """
    dist_ecul=0
    for i in range (len(U)):
        dist_ecul += ((U[i]-V[i])**2)
    return (dist_ecul**0.5)

def dist_linf(U,V):
    """
    >>>dist_linf([ 1 , 2, 4 ],[ 4 , 7, 10 ])
    6
    """
    dist_inf=0
    for i in range (len(U)):
        dist_inf = max(dist_inf,abs(U[i]-V[i]))
    return (dist_inf)

def promedio(U):
    """
    >>>promedio([ 1 , 2, 4 ])
    2.3333333333333335
    """
    miu=0
    for i in range (len(U)):
        miu += U[i]
    return (miu/len(U))

def Desv_est(U):
    """
    >>>Desv_est([ 1 , 2, 4 ])
    1.247219128924647
    """
    lam=0
    prom= promedio(U)
    for i in range (len(U)):
        lam += (U[i]-prom)**2
    return ((lam/len(U))**0.5)

def varianza(U):
    """
    >>>varianza([ 1 , 2, 4 ])
    1.5555555555555554
    """
    return (Desv_est(U) ** 2)

