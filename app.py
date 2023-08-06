import redis
import json

red = redis.Redis(
    host='redis-19252.c16.us-east-1-3.ec2.cloud.redislabs.com',
    port=19252,
    password='B3qhvgBqonPB6ldTLnfJ269BAC4R5vmf'
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break