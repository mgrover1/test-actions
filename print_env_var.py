import os
import act

var = os.getenv('SAMPLE_SECRET')
username = os.getenv('ARM_USERNAME')
token = os.getenv('TOKEN')

print(var)
print(type(username))
print(type(token))
print(len(username))
print(len(token))
print(username)
print(token)

files = act.discovery.download_data(username, token, 'sgpceilC1.b1', '2017-01-14', '2017-01-19')
print(len(files))
