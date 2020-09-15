import json

numbers = [2,3,6,7,11,13]
filename='numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    ns=json.load(f)    
print(ns)