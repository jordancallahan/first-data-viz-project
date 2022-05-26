import matplotlib.pyplot as plt

from random_walk import RandomWalk

# This visualization simulates the path of a pollen grain on the surface of a drop of water.
# Keep making new walks, as long as the program is active.
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(
        rw.x_values,
        rw.y_values,
        c="red",  # type: ignore
        linewidth=3,
    )

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
