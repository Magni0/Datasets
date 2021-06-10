from json import dumps, loads
from faker import Faker
from random import choice, randint
import pytz

fake = Faker()

dataset = []

with open("Datasets/order.json", "r") as file:
    orders = loads(file.read())

with open("Datasets/providers.json", "r") as file:
    providers = loads(file.read())


num = 1
for order in orders:

    provider = choice(providers)

    dataset.append({
        "model": "db.booking",
        "pk": num,
        "fields": {
            "order_id": order['pk'],
            "provider_services_id": provider['pk'],
            "start_time": str(fake.date_time(tzinfo=pytz.UTC)),
            "end_time": str(fake.date_time(tzinfo=pytz.UTC)),
            "guests_number": randint(1, 7),
            "total_price": randint(350, 3500),
        }
    })

    num += 1

with open("Datasets/booking.json", 'w') as file:
    file.write(dumps(dataset))
