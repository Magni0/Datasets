from json import dumps, loads
from random import choice, getrandbits, randint
from faker import Faker

fake = Faker()

dataset = []

with open("Datasets/order.json", "r") as file:
    orders = loads(file.read())

with open("Datasets/messageroom.json", "r") as file:
    users = loads(file.read())

num = 1
for i in orders:
    
    friendliness_rating = randint(1, 7)
    local_expertise_rating = randint(1, 7)
    communication_rating = randint(1, 7)
    value_rating = communication_rating + local_expertise_rating + friendliness_rating

    dataset.append({
        "model": "db.reviewrating",
        "pk": num,
        "fields": {
            "order_id": i['pk'],
            "reviewer_id": randint(1, 50),
            "reviewee_id": randint(51, 100),
            "review_content": fake.sentence(),
            "is_published": bool(getrandbits(1)),
            "friendliness_rating": friendliness_rating,
            "local_expertise_rating": local_expertise_rating,
            "communication_rating": communication_rating,
            "value_rating": value_rating,
        }
    })

    num += 1

with open("Datasets/reviewrating.json", 'w') as file:
    file.write(dumps(dataset))
