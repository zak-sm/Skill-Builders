import requests
import json
from operator import itemgetter

url ='https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)

print(f'Status code: {r.status_code}')

stories_dict = r.json()

submission_dits = []
for story in stories_dict[:5]:
#! New APU call to get details of each submission
    story_url = f'https://hacker-news.firebaseio.com/v0/item/{story}.json'
    r_story = requests.get(story_url)
    print(f'Submission ID: {story}  Status code: {r_story.status_code}')
    story_dict = r_story.json()
    
    #build a dit for each story
    dict_dict = {
        'title': story_dict['title'],
        'link': f'https://news.ycombinator.com/item?id={story}',
        'comments': story_dict['descendants'],
    }
    submission_dits.append(dict_dict)


submission_dicts = sorted(submission_dits, key=itemgetter('comments'),
reverse=True) # sorted(data, item that we are sorting by, do we want to sort in ascending or descending order)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")
