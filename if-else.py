user = {'admin': True, 'active': True, 'name': 'Abhishek'}
prefix = ""

if user['admin'] and user['active']:
    prefix = "ACTIVE - (ADMIN)"
elif user['admin']:
    prefix = "(ADMIN)"
elif user['active']:
    prefix = "ACTIVE -"
print(f"prefix + user['name']")
