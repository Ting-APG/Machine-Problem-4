from math import*
import numpy as np
import matplotlib.pyplot as pl

def ProjectileMotion(h,Vi,angle,Ax,Ay):
    if Ay >= 0:
        print('Please Enter another Value of Acceleration')
        return;
    else:
        AngleR = angle*(pi/180)
        ViX = Vi*cos(AngleR) 
        ViY = Vi*sin(AngleR)
        maxT = np.max(np.roots([0.5*Ay,ViY,h]))
    t = np.linspace(0, maxT, 1000);
    x = ViX*t + 0.5*Ax*(t**2);
    y = ViY*t + 0.5*Ay*(t**2) + h;
    pl.plot(x,y, label='Projectile of y and x');
    pl.xlabel("x")
    pl.ylabel("y")
    pl.legend(loc = "upper right")
    pl.show()
    return;

