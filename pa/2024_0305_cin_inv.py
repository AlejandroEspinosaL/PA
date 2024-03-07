import math

def cin_inv(x,y,z,a1=1,a2=1,a3=1):
    """
    cin_inv(1,1,1)
    return(0.7853981633974483, -0.7853981633974481, 178.9528024488034)
    
    #Este programa sirve para conocer el angulo de los tres motores en un brazo de 3 articulaciones
    #con solo conocer previamente lo largo del brazo y buscando el punto final, la explicacion
    #de la formulas estan en el video "https://youtu.be/D93iQVoSScQ?si=Gz0Im91TsseyDv7y"
    """
    ang1= math.atan2(x, y)
    r1= ((x)**2+(y)**2)**0.5
    r2= z-a1
    o2= math.atan2 (r2,x)
    r3= ((r1)**2+(r2)**2)**0.5
    o1= math.acos((a3**2-(a2)**2-(r3)**2)/(-2*a2*r3))
    ang2= o2-o1
    o3= math.acos(((r3**2)-(a2**2)-(a3*2))/(-2*a2*a3))
    ang3=180-o3
    return(ang1,ang2,ang3)

def cin_inv_simp(x,y,z,a1=1,a2=1,a3=1):
    """
    cin_inv(1,1,1)
    return(0.7853981633974483, -0.7853981633974481, 178.9528024488034)
    
    #este programa hace lo mismo que el anterior pero sin crear tantas variables, solo haciendo los 3
    #calculos de los angulos de manera en que es mucho mas largo pero son menos lineas de codigo
    """
    ang1= math.atan2(x, y)
    ang2= math.atan2 (z-a1,x)-(math.acos((a3**2-(a2)**2-(((((x)**2+(y)**2)**0.5)**2+(z-a1)**2)**0.5)**2)/(-2*a2*(((((x)**2+(y)**2)**0.5)**2+(z-a1)**2)**0.5))))
    ang3= 180-(math.acos((((((((x)**2+(y)**2)**0.5)**2+(z-a1)**2)**0.5)**2)-(a2**2)-(a3*2))/(-2*a2*a3)))
    return(ang1,ang2,ang3)
