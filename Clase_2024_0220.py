def dist_l1(U,V):
    disttax=0
        for i in range (len(U)):
            disttax += abs(U[i]-V[i])
    return (disttax)

def dist_l2(U,V):
    distecul=0
        for i in range (len(U))
        distecul += ((U[i]-V[i])**2)**0.5
    return (distecul)

def dist_linf(U,V):
    distinf=0
        for i in range (len(U))
        distinf = max(distinf,(U[i]-V[i]))
    return (distinf)

def promedio(U):
    miu=0
        for i in range (len(U))
        miu += U[i]
    return (miu/ len(U))

def Desv_est(U):
    lam=0
    prom= promedio(U)
        for i in range (len(U))
        lam += U[i]-prom
    return ((lam/ len(U))**0.5)

def varianza(U):
    var= Desv_est(U)
    return (var**0.5)
