from flask import jsonify
from deta import Deta

# Key for accessing Base
deta = Deta("YOUR_PROJECT_KEY")
# Create "users" table in Base
users = deta.Base('users')

# function for get all user
def get_users():
    all_user = users.fetch()._items
    return jsonify(all_user)

# function for get user by key
def user_detail(key):
    user = users.get(key)
    return user if user else (jsonify({"message":"Not Found"}), 404)

# function for insert new user
def insert_user(name, address, email, password):
    user = users.put({
        "name": name,
        "address": address,
        "email": email,
        "password": password,
    })
    
    return (jsonify(user), 201)

# function login
def login(email, password):
    query = users.fetch({
        "email": email,
        "password": password
    })._items
    # print(query)
    if query:
        return jsonify({"success": True, "message":"Login Successfully", "key": query[0]['key']})
    else:
        return (jsonify({"success": False, "message": "Invalid email/password"}), 404)