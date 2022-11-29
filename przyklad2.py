from collections import ChainMap

user_account = {"id": "PL345354jhk", "type": "konto"}
user_profile = {"name": "JAn kowalski", "type": "profil"}
user = ChainMap(user_account, user_profile)

print(user["id"])
print(user["name"])
print(user["type"])

user["name"] = "Pokemon"
user["name"] = "Mickiewicz"
print(user["name"])
print(user_profile)
print(user_account)
print(user)
