import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)  # type: ignore

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.ticklabel_format(style="plain")
ax.axis([0, 1100, 0, 1_100_000])
ax.tick_params(axis="both", labelsize=14)

plt.tight_layout()
plt.savefig("squares_plot.png")
