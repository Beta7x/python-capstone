from flask import jsonify
from deta import Deta

# Key for accessing Base
deta = Deta("c0zvsjcl_ipGpTywvATheDMQY9Vnm6rqjJDGTPhFc")

# Create table in Base
users = deta.Base('users')
visitors = deta.Base('visitors')

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
    
# function for insert new visitor
def insert_visitor(name, phone, address, message):
    visitor = visitors.put({
        "name": name,
        "phone": phone,
        "address": address,
        "message": message,
    })
    
    return (jsonify(visitor, {"message": "visitor added!"}), 201)

# function for get all visitor
def get_visitors():
    all_visitor = visitors.fetch()._items
    return jsonify(all_visitor)

# function for get visitor by key
def visitor_details(key):
    visitor = visitors.get(key)
    return visitor if visitor else (jsonify({"message": "Not found"}), 404)