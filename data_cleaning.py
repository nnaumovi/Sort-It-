import pandas as pd


def separate():
    df = pd.read_csv('apps.csv', encoding='windows-1252')
    ids = df['id']
    names = df['name']
    keywords = df['keywords'].str.split(', ')

    apps = []
    for i in range(0, names.size):
        keys = []
        keys.extend(keywords[i][1:])
        if "Inc." in keys:
            keys.remove("Inc.")
        if len(keys) > 1:
            apps.append({'title': [names[i]], 'keywords': keys[:-2], 'cat': keys[1]})

    dict = {'f1':[], 'f2':[], 'f3':[], 'f4':[], 'f5':[]}

    for i in range(0, 100):
        dict["f1"].append(apps[i])
        i += 1
        dict["f2"].append(apps[i])
        i += 1
        dict["f3"].append(apps[i])
        i += 1
        dict["f4"].append(apps[i])
        i += 1
        dict["f5"].append(apps[i])

    return dict
