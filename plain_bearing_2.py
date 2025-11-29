import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 基本数据
B = 150.0        # 轴承有效宽度 B (mm)
p0 = 0.0         # 两端压力为 0
p_mid = 1.523    # 中截面压力 4' kPa*100
p_side = 1.224   # B/4 处压力 8' kPa*100

# x 方向上 5 个特征点位置
x_pts = np.array([0, B/4, B/2, 3*B/4, B])
p_pts = np.array([p0, p_side, p_mid, p_side, p0])

# 用样条插值生成光滑曲线
cs = CubicSpline(x_pts, p_pts)
x_fine = np.linspace(0, B, 400)
p_fine = cs(x_fine)

# 绘图
fig, ax = plt.subplots(figsize=(6, 4))

# 压力分布光滑曲线
ax.plot(x_fine, p_fine, color="black", linewidth=1.8)

# 0压力基线
ax.hlines(0, 0, B, colors="black", linewidth=1, linestyles="dashed")

# 左右端竖线（标出两个 0）
# ax.vlines(0, 0, max(p_pts)*1.1, colors="black", linewidth=1)
# ax.vlines(B, 0, max(p_pts)*1.1, colors="black", linewidth=1)
ax.text(-3, 0, "0", va="top", ha="right", fontsize=9)
ax.text(B+3, 0, "0", va="top", ha="left", fontsize=9)

# B/4 与 3B/4 处的竖线 + 标注 8'
ax.vlines(B/4, 0, p_side, colors="gray", linestyles="dashed")
ax.vlines(3*B/4, 0, p_side, colors="gray", linestyles="dashed")
ax.text(B/4, p_side, "8'", ha="center", va="bottom", fontsize=9)
ax.text(3*B/4, p_side, "8'", ha="center", va="bottom", fontsize=9)

# 中截面 4'
ax.vlines(B/2, 0, p_mid, colors="gray", linestyles="dashed")
ax.text(B/2, p_mid, "4'", ha="center", va="bottom", fontsize=9)

y_dim = -0.15 * max(p_pts if p_pts.max() != 0 else 1)

# 美化坐标轴
ax.set_xlim(-0.05*B, 1.15*B)
ax.set_ylim(y_dim*1.5, max(p_pts)*1.2)
# ax.set_xticks([])
# ax.set_yticks([])
ax.set_xlabel("轴向位置")
ax.set_ylabel("压力")

plt.title("轴承轴向油膜压力分布曲线（400N） （Drawn by HZQ）")
plt.tight_layout()
plt.savefig(r"output\\plain_bearing_0_8_400N.png", dpi=300)
plt.show()
