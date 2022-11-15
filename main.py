import controller
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# endpoint for index
@app.route('/')
def index():
    return jsonify({"message": "Index route"})

# endpoint for get all user
@app.route('/users')
def get_all_user():
    return controller.get_users()

# endpoint for get user by key
@app.route('/users/<key>')
def get_user_by_key(key):
    result = controller.user_detail(key)
    return result

# endpoint for insert new user
@app.route('/users/add', methods=['POST'])
@cross_origin()
def new_user():
    details = request.get_json()
    name = details['name']
    address = details['address']
    email = details['email']
    password = details['password']
    
    result = controller.insert_user(
        name, address, email, password
    )
    return result

# endpoint for login
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    result = controller.login(email, password)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)