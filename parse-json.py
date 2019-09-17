import json
with open('persons.json', 'r') as f:
    my_dict = json.load(f)

for distro in my_dict:
    print(distro['gender'])
    print(distro['name'])
