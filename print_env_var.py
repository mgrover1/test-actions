import os

var = os.getenv('SAMPLE_SECRET')
username = os.getenv('ARM_USERNAME')
token = os.getenv('ARM_TOKEN')

print(var)
print(type(username))
print(type(token))
