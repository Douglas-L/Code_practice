import requests
import json

# Standard port
base_url = 'http://127.0.0.1:5000/user/'

# # Get entry
# url = f'{base_url}Nicholas'
# r = requests.get(url)
# print(r.status_code)
# print(r.text)

# # Create new entry
# url = f'{base_url}Johnny' 
# payload = {'age':30, 'occupation':'Barber'}
# r = requests.post(url, data=payload)
# print(r.status_code)
# print(r.text)

# Update an entry
url = f'{base_url}Johnny' 
payload = {'age':31, 'occupation':'Barber'}
r = requests.put(url, data=payload)
print(r.status_code)
print(r.text)
