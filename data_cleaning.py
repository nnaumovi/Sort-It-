import pandas as pd

df = pd.read_csv('app_info.csv')

names = df['name']
categories = df['category']
df['compatibility']=df['compatibility'][:].str.split(' ')
compatibility = df['compatibility']

for elem in compatibility:
    if 'and' in elem:
        elem.remove('and')
    if 'touch.' in elem:
        elem.remove('touch.')

apps = []
for i in range(0, names.size):
    keywords = []
    keywords.append(names[i])
    keywords.append(categories[i])
    keywords.extend(compatibility[i][7:])
    apps.append({'title': [names[i]], 'keywords': keywords, 'cat': [categories[i]]})
print(apps)
