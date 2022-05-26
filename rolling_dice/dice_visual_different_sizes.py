from plotly.graph_objects import Bar, Layout, Figure

from die import Die

# Create two dice of different sizes.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(
    title=f"Results of rolling one D{die_1.num_sides} dice and one D{die_2.num_sides} dice {len(results):,} times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)

fig = Figure(data=data, layout=my_layout)

fig.write_image("two_diff_dice.png")
fig.show()
