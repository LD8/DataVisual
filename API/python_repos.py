import requests
from plotly.graph_objs import Bar
from plotly import offline

# prepare to make an API call: store url and headers in vars
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# explicitly ask to use this version of github API, 
# you can find it here: https://developer.github.com/v3/
headers = {'Accept': 'application/vnd.github.v3+json'}

# make the API call using get() function, 
# and store the response in a variable:
r = requests.get(url, headers=headers)

# check whether the call is successful:
print('Status code: {}'.format(r.status_code))

# type(r) is <class 'requests.models.Response'>
# type(r.json()) is <class 'dict'>
response_dict = r.json()

# print(response_dict.keys())
# dict_keys(['total_count', 'incomplete_results', 'items'])

repos = response_dict['items']

repo_links, repo_descriptions, repo_starcounts = [], [], []

for repo in repos:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_links.append(f'<a href="{repo_url}">{repo_name}</a>')
    owner = repo['owner']['login']
    description = repo['description']
    repo_descriptions.append(f"{owner}<br>{description}")
    repo_starcounts.append(repo['stargazers_count'])

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': repo_starcounts,
    'hovertext': repo_descriptions,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25,25,25)'
        },
    },
    'opacity': 0.6,
}]

layout = {
    'title': 'Top 30 Python Repos',
    'titlefont': {
        'size': 28,
    },
    'xaxis': {
        'title': 'Repositories', 
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars', 
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='top_python_repos.html')