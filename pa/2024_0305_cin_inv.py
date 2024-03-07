import math
def cin_inv(x,y,z,a1=1,a2=1,a3=1):
    ang1= atan2(x, y)
    r1=((x)**2+(y)**2)**0.5
    r2=z-a1
    o2= atan2 (r2,x)
    r3= ((r1)**2+(r2)**2)**0.5
    o1= acos(((a3)**2-(a2)**2-(r3)**2)/(-2*a2*r3))
    ang2= o2-o1
    o3= acos(((r3)**2-(a2)**2-(a3)*2)/(-2*a2*a3))
    ang3=180-o3
return(ang1,ang2,ang3)
