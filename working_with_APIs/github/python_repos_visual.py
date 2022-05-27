import requests

from plotly.graph_objects import Figure

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict["items"]
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict["stargazers_count"])
    label = repo_dict["description"]
    labels.append(label)

# Make visualization.
data = [
    {
        "type": "bar",
        "x": repo_links,
        "y": stars,
        "hovertext": labels,
        "marker": {
            "color": "rgb(60, 100, 150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
        },
        "opacity": 0.6,
    }
]
my_layout = {
    "title": "Most-Starred Python Projects on Github",
    "titlefont": {"size": 28},
    "xaxis": {
        "title": "Repository",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
    "yaxis": {
        "title": "Stars",
        "titlefont": {"size": 24},
        "tickfont": {"size": 14},
    },
}

fig = Figure(data=data, layout=my_layout)

# Comment out below to create html files and images of the visualization.
# fig.write_image("python_repos.png")
# fig.write_html("python_repos.html")
fig.show()
