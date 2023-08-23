def sumaplx (c1,c2):
    perfect = c1[0] + c2[0]
    ent = c1[1] + c2[1]
    return [perfect,ent]
print("La suma da: ",sumaplx((3,2),(-5,5.2)))

def mult (c1,c2):
    par1 = (c1[0]*c2[0]) - (c1[1]*c2[1])
    par2 = (c1[0]*c2[1]) + (c2[0]*c1[1])
    return [par1,par2]
print("La multiplicaciom da: ",mult((3,2),(-5,5.2)))

def div (c1,c2):
    par1 = ((c1[0]*c2[0]) + (c1[1]*c2[1]))
    par2 = ((c2[0]*c1[1]) - (c1[0]*c2[1]))
    div = (c2[0]**2 + c2[1]**2)
    return [par1/div, par2/div]
print("La division da: ",div((3,2),(-5,5.2)))

def modulo (c1):
    return (c1[0]**2+c1[1]**2)**(1/2)
print("El modulo da: ",modulo((3,2)))

def conjugado (c1):
    return [c1[0],-c1[1]]
print("El conjugado da: ",conjugado((3,2)))

import math

def cartesianas_polares (radio, angulo):
    grados = (angulo* math.pi)/180
    x = radio * math.cos(grados)
    y = radio * math.sin(grados)
    return [x,y]
print("Las coordenas cartesianas son: ", cartesianas_polares(6,30))

def fase (c1,c2):

