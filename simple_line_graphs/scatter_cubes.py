import matplotlib.pyplot as plt
from matplotlib import ticker

x_values = range(1, 5_001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.RdPu)  # type: ignore

ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Cubed", fontsize=14)

ax.ticklabel_format(style="plain")
ax.tick_params(axis="both", labelsize=10)
ax.get_xaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, p: format(int(x), ","))
)
ax.get_yaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, p: format(int(x), ","))
)

plt.tight_layout()
plt.savefig("cubes_plot.png")
