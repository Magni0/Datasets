from json import loads, dumps
from random import randint, getrandbits

dataset = []

with open("Datasets/providers.json", "r") as file:
    providers = loads(file.read())

pk = 1
for provider in providers:
    if 1 in provider['fields']['services']:
        dataset.append({
            "model": "db.firsttimerassistanceservice",
            "pk": pk,
            "fields": {
                "provider": provider['pk'],
                "price_per_hour": randint(50, 500),
            }
        })

        pk += 1

with open("Datasets/15_firsttimeservices.json", "w") as file:
    file.write(dumps(dataset))