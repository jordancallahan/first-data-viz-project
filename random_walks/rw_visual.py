import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    rw = RandomWalk(100_000)
    rw.fill_walk()

    plt.style.use("seaborn")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.RdPu,  # type: ignore
        edgecolors="none",
        s=1,
    )
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
