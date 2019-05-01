# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


import control
import matplotlib.pyplot as plt
import numpy as np


num = [0.7 , 2]
den = [1 , 1.5 , 2]

sys = control.TransferFunction(num,den)



# You can quickly control this by typing built-in magic commands in Spyder's IPython console, which I find faster than picking these from the preferences menu. Changes take immediate effect, without needing to restart Spyder or the kernel.
# To switch to "automatic" (i.e. interactive) plots, type:
# Escribir en la consola!         %matplotlib auto
# Escribir en la consola!         %matplotlib inline    para escribir en la consola

control.bode_plot(sys)
print(control.pole(sys))
print(control.zero(sys))
control.pzmap(sys)

t, y = control.step_response(sys)
plt.figure(3)
plt.plot(t, y, 'r')
plt.ylabel('Xp(t)')
plt.xlabel('Xin(t)')

print(control.tf2ss(sys))
