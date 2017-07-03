#!/usr/bin/env python3
# Encoding:UTF-8
# Filename: print love.py

for yy in range(20,-20,-2):
    for xx in range(-30,30,1):
        y=yy/10
        x=xx/10
        if (x*x+y*y-1)*(x*x+y*y-1)*(x*x+y*y-1)<=x*x*y*y*y:
            print('*',end="")
        else:
            print(' ',end="")
    print()