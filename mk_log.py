file_path = "./sample.json"

data = {}
data['logIn'] = []
data['logIn'].append({
    "step1": True,
    "step2": False,
    "step3": True
})
data['logIn'].append({
    "step1": False,
    "step2": True,
    "step3": True
})
print(data)

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)