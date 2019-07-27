#!/usr/bin/env python3.7

import requests
import datetime

repos = [
    'realtux/keyval',
    'engineer-man/emkc',
    'engineer-man/piston',
    'engineer-man/felix',
]

results = []

for repo in repos:
    commits = requests.get(f'https://api.github.com/repos/{repo}/commits').json()

    last_commit = 'None'

    commit = commits[0]

    now = datetime.datetime.now()
    then = datetime.datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')
    diff = (now-then).days

    results.append({
        'repo': repo,
        'last': then,
        'since': diff,
    })

print('repos last updated:')

for result in results:
    print('{}: {} ({} days ago)'.format(result['repo'], result['last'], result['since']))
