import pandas as pd
import matplotlib.pyplot as plt

# 读取 excel
df = pd.read_excel(r"data\\带传动.xlsx")

# 画图
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax1 = plt.subplots(figsize=(8, 4))

x = df["T2(N·mm)"]        # 横坐标T2
y_eps = df["ε(%)"]        # 左轴ε
y_eta = df["η(%)"]        # 右轴η

# 左纵轴：T2-ε 曲线（蓝色）
line1 = ax1.plot(
    x, y_eps,
    color="blue", marker="D", linestyle="-", linewidth=2,
    label="T$_2$-ε曲线"
)
ax1.set_xlabel("T$_2$(N·mm)")

# 隐藏默认左轴标签
ax1.set_ylabel("")

# 右纵轴：T2-η 曲线（红色）
ax2 = ax1.twinx()
line2 = ax2.plot(
    x, y_eta,
    color="red", marker="s", linestyle="-", linewidth=2,
    label="T$_2$-η曲线",
)
ax2.set_ylabel("")

# 左、右轴文字，上方显示
ax1.text(
    0, 1.02, "ε(%)",
    transform=ax1.transAxes,
    ha="center", va="bottom", fontsize=14
)

ax2.text(
    1, 1.02, "η(%)",
    transform=ax2.transAxes,
    ha="center", va="bottom", fontsize=14
)

# 合并图例
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

# 网格、边距等
ax1.grid(True, linestyle="--", alpha=0.5)

plt.title("带传动：效率和滑动率曲线 （Drawn by HZQ）", fontsize=16, pad=15, weight="bold", loc="center")
plt.tight_layout()
plt.savefig(r"output\\belt_driving_better.png", dpi=300)
plt.show()
