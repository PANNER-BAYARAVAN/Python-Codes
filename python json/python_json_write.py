import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'John',
    'website': 'aa.com',
    'from': 'selangor'
})
data['people'].append({
    'name': 'Ali',
    'website': 'bb.com',
    'from': 'kedah'
})
data['people'].append({
    'name': 'Tim',
    'website': 'cc.com',
    'from': 'perlis'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)