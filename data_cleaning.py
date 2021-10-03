import pandas as pd

df = pd.read_csv('apps.csv', encoding='windows-1252')
ids = df['id']
names = df['name']
keywords = df['keywords'].str.split(', ')

apps = []
for i in range(0, names.size):
    keys = []
    keys.extend(keywords[i][1:])
    if len(keys) > 1:
        apps.append({'title': [names[i]], 'keywords': keys[:-2], 'cat': keys[1]})
