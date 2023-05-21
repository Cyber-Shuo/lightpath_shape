import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist
from scipy.interpolate import make_interp_spline

X_s,Y_s = [],[]
with open('D:\\STUDY_think\\Data\\ALL_Figure\\python_fig\\python_light_shape\\nolens.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X_s.append(value[0])
        Y_s.append(value[1])

Y_s = np.array(Y_s)/2
X_s_smooth = np.linspace(0, 1300, 13000)
Y_s_smooth = make_interp_spline(X_s, Y_s)(X_s_smooth)

X_l,Y_l = [],[]
with open('D:\\STUDY_think\\Data\\ALL_Figure\\python_fig\\python_light_shape\\lens19.5cm.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X_l.append(value[0])
        Y_l.append(value[1])

Y_l = np.array(Y_l)/2
X_l_smooth = np.linspace(200, 1300, 12800)
Y_l_smooth = make_interp_spline(X_l, Y_l)(X_l_smooth)

plt.plot(X_s, Y_s, color = 'b', label = 'no lens', marker="o", markersize=10)
plt.plot(X_l, Y_l, color = 'r', label = r'$l_{long}$', marker="x", markersize=10)
plt.fill_between(X_s, Y_s, Y, color = 'b', alpha = 0.3)
plt.fill_between(X_l, Y_l, Y, color = 'r', alpha = 0.5)
plt.plot(X_s_smooth, Y_s_smooth, color = 'black', label = 'Interpolation method envelope')
plt.plot(X_l_smooth, Y_l_smooth, color = 'black')

plt.xlabel('Light source to PMT distance/mm')
plt.ylabel('Spot radius/mm')
plt.legend()
plt.title('Optical path comparison')
plt.show()

