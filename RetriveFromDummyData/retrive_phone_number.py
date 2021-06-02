import json

phone_number = []

with open('DummyData/Resorts.json', 'r') as file:
    raw = file.read()
    content = json.loads(raw)
    [phone_number.append(i['Phone']) for i in content if i['Phone'] not in phone_number]

u = [i.replace('"', '') for i in phone_number]

# write countrys to file
with open('output/PhoneNumber.txt', 'a') as f:
    for x in u:
        f.write(x + "\n")