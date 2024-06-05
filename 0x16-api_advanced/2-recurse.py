#!/usr/bin/python3
'''Module containing functions for working
    with the Reddit API
'''
import requests

BASE_URL = 'https://www.reddit.com'

def top_ten(subreddit):
    api_headers = { 
            'Accept': 'application/json',
            'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36'
            'Edge/97.0.1072.62'
        ])
    }
    sort = 'top'
    limit = 10
    res = requests.get(
            '{}/r/{}/.json?sort={}&limit={}'.format(
                BASE_URL,
                subreddit,
                sort,
                limit,
                ),
            headers = api_headers,
            allow_redirects = False
    )
    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
             return recurse(subreddit, hot_list, n + count, data['after'])
        else:
             return hot_list if hot_list else None
    else:
         return hot_list if hot_list else None
