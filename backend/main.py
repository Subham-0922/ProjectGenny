from flask import Flask, jsonify, request
from models.database import user, projects, tasks, resource, activeUser
from service.authLog import signUp,logIn,logout
app = Flask(__name__)

@app.route('/signup')
def dosignUp():return signUp(request.get_json())

@app.route('/login')
def doLogIn():return logIn(request.get_json())
@app.route('/logout/<email>')
def doLogOut(email):return logout(email)

# response={
#     'secretKey':'Jenny',
#     'user':createUser('Subham-Main','Burnwal','Admin','Senio','ksubham789@gmail.com','545454')
#
# }



if __name__ == '__main__':
    app.run(debug=True)

