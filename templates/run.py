from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/user',methods=['POST'])
def PostInput():
    InputValue = request.get_json()
    em = InputValue['email']
    pw = InputValue['password']
    input1 = em
    input2 = pw
    print(input1,input2)

    return jsonify({'return':'OK!'})


class user:
    def __init__(self,email,password) -> None:
        self.email = email
        self.password = password

    def __repr__(self):
        return f' <user:{self.email}>'

users = []
users.append(user(email='b07612041',password='123'))

print(users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)