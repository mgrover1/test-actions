import os

var = os.getenv('SAMPLE_SECRET')
username = os.getenv('ARM_USERNAME')
token = os.get_env('ARM_TOKEN')

print(var)
print(type(username))
print(type(token))
