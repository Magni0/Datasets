from json import loads, dumps
from random import randint, getrandbits

dataset = []

with open("Datasets/providers.json", "r") as file:
    providers = loads(file.read())

pk = 1
for i in providers:
    if bool(getrandbits(1)) and bool(getrandbits(1)):
        dataset.append({
            "model": "db.firsttimerassistanceservice",
            "pk": pk,
            "fields": {
                "provider": i['pk'],
                "price_per_hour": randint(50, 500),
            }
        })

        pk += 1

with open("Datasets/firsttimeservices.json", "w") as file:
    file.write(dumps(dataset))