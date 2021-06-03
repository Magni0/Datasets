from json import dumps, loads
from random import randint

ski_backcountry_service_dataset = []
snowboarding_backcountry_service_dataset = []
snowshoeing_service_dataset = []
snowmobiling_service_dataset = []
bikeriding_service_dataset = []

with open("Datasets/providers.json", "r") as file:
    providers = loads(file.read())

num = 1
for service in providers:
    if randint(1, 4) == 1:
        ski_backcountry_service_dataset.append({
            "model": "db.skibackcountryservice",
            "pk": num,
            "fields": {
                "provider": service['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for service in providers:
    if randint(1, 4) == 1:
        snowboarding_backcountry_service_dataset.append({
            "model": "db.snowboardingbackcountryservice",
            "pk": num,
            "fields": {
                "provider": service['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for service in providers:
    if randint(1, 4) == 1:
        snowshoeing_service_dataset.append({
            "model": "db.snowshoeingservice",
            "pk": num,
            "fields": {
                "provider": service['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for service in providers:
    if randint(1, 4) == 1:
        snowmobiling_service_dataset.append({
            "model": "db.snowmobilingservice",
            "pk": num,
            "fields": {
                "provider": service['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for service in providers:
    if randint(1, 4) == 1:
        bikeriding_service_dataset.append({
            "model": "db.bikeridingservice",
            "pk": num,
            "fields": {
                "provider": service['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

with open("Datasets/22_skibackcountryservice.json", "w") as file:
    file.write(dumps(ski_backcountry_service_dataset))

with open("Datasets/23_snowboardingbackcountryservice.json", "w") as file:
    file.write(dumps(snowboarding_backcountry_service_dataset))

with open("Datasets/25_snowshoeingservice.json", "w") as file:
    file.write(dumps(snowshoeing_service_dataset))

with open("Datasets/24_snowmobilingservice.json", "w") as file:
    file.write(dumps(snowmobiling_service_dataset))

with open("Datasets/21_bikeridingservice.json", "w") as file:
    file.write(dumps(bikeriding_service_dataset))
