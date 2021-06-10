from json import dumps, loads
from random import randint

ski_tour_service_dataset = []
snowboard_tour_service_dataset = []
walking_tour_service_dataset = []
ebike_touring_service_dataset = []
hiking_service_dataset = []

with open("Datasets/providers.json", "r") as file:
    providers = loads(file.read())

num = 1
for skitourservice in providers:
    if 5 in skitourservice['fields']['services']:
        ski_tour_service_dataset.append({
            "model": "db.skitourservice",
            "pk": num,
            "fields": {
                "provider": skitourservice['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for snowboardtourservice in providers:
    if 6 in snowboardtourservice['fields']['services']:
        snowboard_tour_service_dataset.append({
            "model": "db.snowboardtourservice",
            "pk": num,
            "fields": {
                "provider": snowboardtourservice['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for walkingtourservice in providers:
    if 7 in walkingtourservice['fields']['services']:
        walking_tour_service_dataset.append({
            "model": "db.walkingtourservice",
            "pk": num,
            "fields": {
                "provider": walkingtourservice['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for ebiketouringservice in providers:
    if 8 in ebiketouringservice['fields']['services']:
        ebike_touring_service_dataset.append({
            "model": "db.ebiketouringservice",
            "pk": num,
            "fields": {
                "provider": ebiketouringservice['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

num = 1
for hikingservice in providers:
    if 9 in hikingservice['fields']['services']:
        hiking_service_dataset.append({
            "model": "db.hikingservice",
            "pk": num,
            "fields": {
                "provider": hikingservice['pk'],
                "max_group_size": randint(1, 7),
                "price_per_head": randint(50, 500),
                "additional_guests_price": randint(100, 200)
            }
        })

        num += 1

with open("Datasets/18_skitourservice.json", "w") as file:
    file.write(dumps(ski_tour_service_dataset))

with open("Datasets/19_snowboardtourservice.json", "w") as file:
    file.write(dumps(snowboard_tour_service_dataset))

with open("Datasets/20_walkingtourservice.json", "w") as file:
    file.write(dumps(walking_tour_service_dataset))

with open("Datasets/16_ebiketouringservice.json", "w") as file:
    file.write(dumps(ebike_touring_service_dataset))

with open("Datasets/17_hikingservice.json", "w") as file:
    file.write(dumps(hiking_service_dataset))