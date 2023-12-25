# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:10:04 2021

@author: Eleve
"""
from PIL.Image import *
from math import*
L,H=800,800
x_min,x_max=-2,2
y_min,y_max=-2,2
black=(0,0,0)
white=(255,255,255)
MAX_ITERATION=20

def colorpixel(image,x,y,couleur):
    image.putpixel((x,y),couleur)
    
def distanceOMN(Cx,Cy,n):
    x,y=Calculcoord(Cx,Cy,n)
    return sqrt(x**2+y**2)

def conversion(x,y):
    u=x_min+x*(x_max-x_min)/L
    v=y_max-y*(y_max-y_min)/H
    return u,v

def Calculcoord(Cx,Cy,n):
    x,y=0,0
    for i in range(n):
        temp=x
        x=x**2-y**2+Cx
        y=2*temp*y+Cy
    return (x,y)

def Mandelbrot(MAX_ITERATION):
    image=new('RGB',(L,H))
    for x in range (L):
        for y in range(H):
            u,v=conversion(x,y)
            n=0
            d=distanceOMN (u,v,n)
            while d<2 and n<MAX_ITERATION:
                d=distanceOMN(u,v,n)
                n=n+1
            if n==MAX_ITERATION:
                colorpixel(image,x,y,black)
                
            else:
                colorpixel(image,x,y,white)
    image.show()
                 
                
Mandelbrot(10)
            
            