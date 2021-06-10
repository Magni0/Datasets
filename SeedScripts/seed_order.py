from json import dumps, loads
from random import choice
from faker import Faker

fake = Faker()

dataset = []

statuses = (
    'pending',
    'declined',
    'accepted',
    'paid',
    'cancelled',
    'refund',
)

with open("Datasets/13_paymentmethod.json", "r") as file:
    paymentmethod = loads(file.read())

num = 1
for i in paymentmethod:
    dataset.append({
        "model": "db.order",
        "pk": num,
        "fields": {
            "payment_detail_id": i['pk'],
            "user_id": i['fields']['user_id'],
            "service_charge": 5.00,
            "status": choice(statuses),
            "created_date": fake.date(),
        }
    })

    num += 1

with open("Datasets/order.json", 'w') as file:
    file.write(dumps(dataset))
