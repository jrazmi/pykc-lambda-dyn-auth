from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route('/')
def index():
    return jsonify({
        "hello": "world"
    })


import boto3
session = boto3.Session()
dynDB = session.resource('dynamodb')
table = dynDB.Table('PYKC-Auth')


import bcrypt
import time
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # REQUIRE AN EMAIL AND PASSWORD
    if not data.get('email', None) or not data.get('password', False):
        return jsonify({'error': 'must provide email and password'})

    # VERIFY THAT THIS USER DOES NOT ALREADY EXIST
    check_status = table.get_item(Key={"email": str(data['email']).upper()})
    if(check_status.get('Item')):
        return jsonify({'error': 'profile exists already'})


    #CREATE A HASHED PASSWORD AND POST OBJECT
    hashed_password = bcrypt.hashpw(str(data['password']), bcrypt.gensalt())
    post_obj = {
        'email': data['email'].upper(),
        'password_hash': hashed_password,
        'created_at': int(time.time())
    }

    save_user = table.put_item(
        Item=post_obj
    )

    return jsonify({'message': 'user created'})


import jwt
import datetime
#put this in an env variable
SECRET_KEY='pykc'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    error = {'error': 'invalid user email or password'}
    if not data.get('email', None) or not data.get('password', False):
        return jsonify(error)

    get_user = table.get_item(Key={"email": str(data['email']).upper()})
    user = get_user.get('Item', None)

    if not user:
        return jsonify(error)

    password_hash = user.get('password_hash', None)
    if not bcrypt.checkpw(str(data['password']), str(password_hash)):
        return jsonify(error)

    payload = jwt.encode(
        {
            "sub": user['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm='HS256'
    )

    return jsonify({'token': payload})

from functools import wraps

def unauthorized(message):
	response = jsonify({'error': 'unauthorized', 'message': message})
	response.status_code = 401
	return response

def AuthRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authhead = request.headers.get('Authorization', None)
        if not authhead:
            return unauthorized('authorization required')
        data = str(authhead).encode('ascii','ignore')
        token = str.replace(data, 'Bearer ', '')
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return unauthorized('authorization error')

        return f(*args, **kwargs)
    return decorated

@app.route('/auth')
@AuthRequired
def authcheck():
    return jsonify({"message": "wooohoo"})






if __name__ == "__main__":
    app.run(debug=True)
