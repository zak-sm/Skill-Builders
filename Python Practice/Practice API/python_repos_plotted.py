import requests
import plotly.express as px

#* Make an API call and check the response.
url = "https://api.github.com/search/repositories" #* Main part of the URL
url += "?q=language:python+sort:stars+stars:>10000" #* Added query parameters


headers = {"Accept": "application/vnd.github.v3+json"}

r = requests.get(url, headers=headers) #! We pass the url and headers to create the request

print (f"Status code: {r.status_code}") #! Status code 200 means the request was successful

response_dict = r.json()

#* Process the results
print(response_dict.keys()) #* Print the keys of the response dictionary


print("Total number of repositories:", response_dict["total_count"]) #* Print the total number of repositories
print(f"Complete responses: {not response_dict['incomplete_results']}") #! We use 'not' to reverse the boolean value

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_links, stars, hover_texts = [], [], []

for repo in repo_dicts:
    repo_name = repo['name']
    stars.append(repo['stargazers_count'])
    repo_url = repo['html_url']
    repo_link = f'<a href= "{repo_url}"> {repo_name} </a>'
    repo_links.append(repo_link)
    #* Build Hover Text
    owner = repo['owner']['login']
    description = repo['description']
    hover_text = f'{owner}<br />{description}' #! Plotly lets you use HTML in hover text, here we make a line break
    hover_texts.append(hover_text)

labels = {'x':'Repository Name', 'y':'Stars'}
title = 'Top Python Starred Repositories'

fig = px.bar(x=repo_links, y=stars, labels=labels, title=title, hover_name= hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,yaxis_title_font_size=20) #! Used to modify specific elements
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)


fig.show()
