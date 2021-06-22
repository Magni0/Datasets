import json
import random
from faker import Faker
import pytz

fake = Faker()

dataset = []

with open("Datasets/messageroom.json", "r") as file:
    message_rooms = json.loads(file.read())

pk = 1
for message_room in message_rooms:
    for sender in range(random.randint(1, 5)):
        dataset.append({
            "model": "db.message",
            "pk": pk,
            "fields": {
                "user_id": message_room['fields']['sender_user_id'],
                "message_room_id": message_room['pk'],
                "message_content": fake.sentence(),
                "created_time": str(fake.date_time(tzinfo=pytz.UTC)),
            }
        })
        
        pk += 1
    
    for reciver in range(random.randint(1, 5)):
        dataset.append({
            "model": "db.message",
            "pk": pk,
            "fields": {
                "user_id": message_room['fields']['reciever_user_id'],
                "message_room_id": message_room['pk'],
                "message_content": fake.sentence(),
                "created_time": str(fake.date_time(tzinfo=pytz.UTC)),
            }
        })
        
        pk += 1

with open("Datasets/messages.json", 'w') as file:
    file.write(json.dumps(dataset))
