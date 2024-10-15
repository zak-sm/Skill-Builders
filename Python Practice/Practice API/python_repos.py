import requests

#* Make an API call and check the response.
url = "https://api.github.com/search/repositories" #* Main part of the URL
url += "?q=language:python+sort:stars+stars:>10000" #* Added query parameters


#* Specify the API version and the format of the response (Here being JSON)
headers = {"Accept": "application/vnd.github.v3+json"}

#* We use requests to make a call to the API
r = requests.get(url, headers=headers) #! We pass the url and headers to create the request

#The response object has an attribute called status_code, which tells us whether the request was successful
print (f"Status code: {r.status_code}") #! Status code 200 means the request was successful

#* Now we take the response object and convert it to a Python dictionary using the json module
response_dict = r.json()

#TODO Remeber that the API will only return a maximum of 30 results per page. We can request more results if necessary

#* Process the results
print(response_dict.keys()) #* Print the keys of the response dictionary


#Explore the results of the returned call
print("Total number of repositories:", response_dict["total_count"]) #* Print the total number of repositories
print(f"Complete responses: {not response_dict['incomplete_results']}") #! We use 'not' to reverse the boolean value

#Explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#Examine the first repository
#repo = repo_dicts[0] #*Get the first repository
#print("\nKeys of the first repository:", len(repo)) #*Get the ammount of keys in repository
#for key in sorted(repo.keys()): #*Print the keys in alphabetical order
#    print(key)


for repo in repo_dicts:
    print("\nSelected information about first repository:")
    print(f"Name: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")