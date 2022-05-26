from plotly.graph_objects import Bar, Layout, Figure

from die import Die

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list, using list comprehension.
results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(50_000)]

# Analyze the results, with list comprehension.
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

# Visualize the results.
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title=f"Results of rolling three D{die_1.num_sides} dice {len(results):,} times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)

fig = Figure(data=data, layout=my_layout)

fig.write_image("three_d6_dice.png")
fig.show()
