import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 基本参数
d = 100.0                 # 轴承内径，单位mm 
R = d / 2                 # 半径
k = 50.0                  # 压力→长度比例系数

# 7 个传感器的角度（度）
angles_deg = np.array([150, 130, 110, 90, 70, 50, 30])

# 7 个传感器测得的压力值（单位 kPa*100）

pressures = np.array([1.269, 1.699, 1.741, 1.638, 1.444, 1.1083, 0.813])

# pressures = np.array([1.072, 1.541, 1.580, 1.514, 1.336, 1.005, 0.74])

# 计算圆和压力端点坐标
theta = np.deg2rad(angles_deg)

# 圆周上的点（传感器位置 1~7）
x_circle = R * np.cos(theta)
y_circle = R * np.sin(theta)

# 压力线长度：L = k * p
L = k * pressures

# 压力端点 1'~7'
x_outer = (R + L) * np.cos(theta)
y_outer = (R + L) * np.sin(theta)

# 两端 0、8
extra_angles_deg = np.array([180, 0])
extra_theta = np.deg2rad(extra_angles_deg)
x_extra = R * np.cos(extra_theta)
y_extra = R * np.sin(extra_theta)

# 为了画光滑曲线，把 0、1'~7'、8 组合在一起按角度排序
all_theta = np.concatenate([extra_theta[:1], theta, extra_theta[1:]])
all_r = np.concatenate([[R], R + L, [R]])
all_x = all_r * np.cos(all_theta)
all_y = all_r * np.sin(all_theta)

# 开始画图
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal", "box")

# 画基准圆（轴承中径）
phi = np.linspace(0, np.pi, 200)

ax.plot(R * np.cos(phi), R * np.sin(phi), color="black")

# 画 7 条径向线 1-1' ~ 7-7'
for i, ang in enumerate(angles_deg):
    t = np.deg2rad(ang)

    # 圆周点
    x0, y0 = R * np.cos(t), R * np.sin(t)
    # 外端点
    x1, y1 = x_outer[i], y_outer[i]

    # 画圆心到外端点的线（包括穿过圆周的那一段）
    ax.plot([0, x1], [0, y1], color="black", linewidth=0.8)

    # 标号 1,2,3,... 放在圆周附近
    ax.text(x0*1.05, y0*1.05, str(i+1), ha="center", va="center", fontsize=9)
    
    ax.text(x1*1.05, y1*1.01, f"{i+1}$^'$", fontsize=9)

# 画油膜压力分布光滑曲线（通过 0,1',2',...,7',8）
# 组合 0、1'~7'、8
all_theta = np.concatenate([extra_theta[:1], theta, extra_theta[1:]])
all_r = np.concatenate([[R], R + L, [R]])

# 按角度从小到大排序
idx = np.argsort(all_theta)          # 得到从小到大的索引
theta_sorted = all_theta[idx]
r_sorted = all_r[idx]

# 使用三次样条插值
cs = CubicSpline(theta_sorted, r_sorted)
theta_fine = np.linspace(theta_sorted.min(), theta_sorted.max(), 400)
r_fine = cs(theta_fine)

x_fine = r_fine * np.cos(theta_fine)
y_fine = r_fine * np.sin(theta_fine)

ax.plot(x_fine, y_fine, color="black", linewidth=1.8)

# 绘制带箭头的 X/Y 坐标轴
# X 轴
ax.annotate(
    "", xy=(2*R, 0), xytext=(-2*R, 0),
    arrowprops=dict(arrowstyle="->", lw=1.2)
)

# Y 轴
ax.annotate(
    "", xy=(0, 2.9*R), xytext=(0, -1*R), 
    arrowprops=dict(arrowstyle="->", lw=1.2)
)

# 坐标轴文字
ax.text(2*R, -2, "X", fontsize=12)
ax.text(-4, 2.8*R, "Y", fontsize=12)

# 适当设置显示范围
ax.set_xlim(-R*2.1, R*2.1)
ax.set_ylim(-R, R*3)
ax.set_xticks([])
ax.set_yticks([])

ax.text(50, -5, 'Drawn by HZQ', fontsize=12, ha='center', va='center')

plt.title("油膜圆周压力分布曲线（600N）", fontsize=14, pad=15, weight="bold", loc="center")

# plt.title("油膜圆周压力分布曲线（400N）", fontsize=14, pad=15, weight="bold", loc="center")

plt.tight_layout()

plt.savefig(r"output\\plain_bearing_600N.png", dpi=300)

# plt.savefig(r"output\\plain_bearing_400N.png", dpi=300)
plt.show()
