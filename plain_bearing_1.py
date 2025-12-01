import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

W1 = 600
W2 = 400
d = 60
B = 125
η = 0.3

f1 = np.array([1.24,0.01,0.03,0.02,0.01,0.02,0.01,0.01,5.76])
n1 = np.array([350, 250, 150, 100, 50, 30, 20, 10, 5])

f2 = np.array([0.52,0.02,0.01,0.02,0.01,0.02,0.01,0.01,5.47])
n2 = np.array([350, 250, 150, 100, 50, 30, 20, 10, 5])

# f3 = np.array([0.02,0.01,0.02,0.01])
# n3 = np.array([250, 150, 100, 50])

# f4 = np.array([0.01,0.03,0.02,0.01])
# n4 = np.array([250, 150, 100, 50])

f = np.flip(f2)
n = np.flip(n2)

p = W2 / (d * B)
λ = n * η / p

x = λ
y = f

X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

print(y)

plt.plot(X_, Y_, linestyle='-')
plt.xlabel('λ')
plt.ylabel('f')
plt.title('滑动系数与滑动率关系曲线（400N） （Drawn by HZQ）')
plt.grid(True)
plt.savefig(r"output\\plain_bearing_f_400N.png", dpi=300)
plt.show()