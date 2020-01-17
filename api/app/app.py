from flask import Flask, render_template, request, make_response, g, jsonify
import os
import socket
import random
import json
import sys
import datetime
import requests
from flask_sqlalchemy import SQLAlchemy
import hashlib
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_cors import CORS

JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY'] 
DATABASE_URI = 'postgres+psycopg2://postgres:password@db:5432/dashboard'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1)
cors = CORS(app, resources={"/*": {"origins": "*"}})

db = SQLAlchemy(app)



class Widgets(db.Model):
    __tablename__ = 'widgets'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    position = db.Column(db.Integer)
    refresh_timer = db.Column(db.Integer)
    type = db.Column(db.String(50))
    datas = db.Column(db.String(300))

    def __init__(self, user_id, position, refresh_timer, type, datas):
        self.user_id = user_id
        self.position = position
        self.refresh_timer = refresh_timer
        self.type = type
        self.datas = datas

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'position': self.position,
            'refresh_time': self.refresh_timer,
            'type': self.type,
            'datas': self.datas,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return (str(self.id)+": [type:"+str(self.type)+"] [pos:"+str(self.position)+"] [datas:"+self.datas+"]")


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    mail = db.Column(db.String(130))    
    password = db.Column(db.String(100))
    widgets = db.relationship('Widgets', uselist=True, lazy=True)

    def __init__(self, username, mail, password):
        self.username = username
        self.mail = mail
        self.password = sha256(password)

    def verify_hash(self, password):
        if (safe_str_cmp(self.password, sha256(password))):
            return (True)
        return (False)

    def serialize(self):
        return {
            'id': self.id, 
            'username': self.username,
            'mail': self.mail,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Id %r Users %r Pass: %r>' % (self.id, self.username, self.password)


def sha256(string):
    res = hashlib.sha256(string.encode()).hexdigest()
    return (res)

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.verify_hash(password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()

jwt = JWT(app, authenticate, identity)

db.create_all()
db.session.commit()

@app.route("/", methods=['POST', 'GET'])
def home():
    return ({'status': 'success', 'message': 'Welcome on Dashboard API.'})

@app.route("/register", methods=['POST'])
def register():
    if (len(request.json) != 3):
        return (jsonify({'status': 'error', 'message': 'bad parameters'}))
    username = request.json['username']
    password = request.json['password']
    mail = request.json['mail']
    if (User.query.filter_by(username=username).first() is None and User.query.filter_by(mail=mail).first() is None):
        new_user = User(username, mail, password)
        new_user.save()
        return ({'status': 'success', 'message': 'Register Success'})
    return ({'status': 'error', 'message': 'this user already exist'})

@app.route('/widgets', defaults={'id': -1}, methods=['POST', 'GET'])
@app.route('/widgets/<int:id>', methods=['POST', 'PUT', 'DELETE'])
@jwt_required()
def widgets(id):
    usr = current_identity
    print(usr.username)
    if (request.method == 'POST' and id == -1):
        num_widget = len(Widgets.query.filter_by(user_id=usr.id).all()) + 1
        new_widget = Widgets(usr.id, num_widget, request.json['refresh_timer'], request.json['type'], request.json['datas'])
        new_widget.save()
        return ({'status': 'success', 'message': 'New widget successfully added'})
    if (request.method == 'GET' and id == -1):
        return (jsonify([widget.serialize() for widget in Widgets.query.filter_by(user_id=usr.id).all()]))
    if ((Widgets.query.filter_by(id=id).first() is None) != True):
        if (request.method == 'PUT'):
            widget = Widgets.query.filter_by(id=id).first()
            widget.refresh_timer = request.json['refresh_timer'] if request.json['refresh_timer'] else widget.refresh_timer
            widget.position = request.json['position'] if request.json['position'] else widget.position
            widget.datas = request.json['datas'] if request.json['datas'] else widget.datas
            widget.save()
            return ({'status': 'success', 'message': "Widget '"+widget.type+"' successfully updated"})
        if (request.method == 'DELETE'):
            type = Widgets.query.filter_by(id=id).first().type
            Widgets.query.filter_by(id=id).first().delete()
            return ({'status': 'success', 'message': "Widget '"+type+"' successfully deleted"})
    return ({'status': 'error', 'message': 'Bad parameters'})

@app.route('/user', defaults={'id': -1}, methods=['GET', 'PUT', 'DELETE'])
@app.route('/user/<int:id>', methods=['DELETE'])
@jwt_required()
def user(id):
    usr = current_identity
    if (request.method == 'GET'):
        return ({'username': usr.username, 'mail': usr.mail})
    if (request.method == 'PUT'):
        print(request.json)
        if (len(request.json) == 1):
            usr.mail = request.json['mail']
        if (len(request.json) == 2):
            usr.password = request.json['password']
        usr.save()
        return ({'status': 'success', 'message': "User information successfully modified"})
    if (request.method == 'DELETE'):
        if (usr.username != "admin"):
            return ({'status': 'success', 'message': 'Your are not allowed to execute this action'})
        if ((User.query.filter_by(id=id).first() is None) != True):
            victim = User.query.filter_by(id=id).first()
            name = victim.username
            victim.delete()
            return ({'status': 'success', 'message': "User '"+name+"' successfully deleted"})
        return ({'status': 'error', 'message': "This user doesn't exist"})    
    return ({'status': 'error', 'message': 'Bad parameters'})

@app.route('/users', methods=['GET'])
@jwt_required()
def list_users():
    usr = current_identity
    if (usr.username != "admin"):
        return ({'status': 'error', 'message': 'Your are not allowed to execute this action'})
    res = [user.serialize() for user in User.query.all()]
    return ({'status': 'success', 'datas': res})

@app.route('/api/<name>/<query>', methods=['GET'])
def internApi(name, query):
    if (name == "trump"):
        return (requests.get('https://api.tronalddump.io/search/quote?query='+query).json())
    if (name == "weather"):
        return (requests.get('https://api.openweathermap.org/data/2.5/weather?q='+query+'&appid=84695e34512f2ca637a048b2c16f97a0').json())
    if (name == "movie_compare"):
        actors = query.split(';')
        id_1 = requests.get('https://api.themoviedb.org/3/search/person?api_key=0d5a9f64db3ef47c0a9e1e447debb789&page=1&query='+actors[0]).json()['results'][0]['id']
        id_2 = requests.get('https://api.themoviedb.org/3/search/person?api_key=0d5a9f64db3ef47c0a9e1e447debb789&page=1&query='+actors[1]).json()['results'][0]['id']
        req = requests.get('https://api.themoviedb.org/3/discover/movie?with_people='+str(id_1)+','+str(id_2)+'&api_key=0d5a9f64db3ef47c0a9e1e447debb789&sort_by=vote_average.desc').json()
        return (req)
    if (name == "best_movie"):
        return (requests.get('http://api.themoviedb.org/3/discover/movie?certification_country='+query+'&certification=R&sort_by=vote_average.desc&api_key=0d5a9f64db3ef47c0a9e1e447debb789').json())
    return ({'status': 'error', 'message': 'bad parameters'})

@app.route('/protected')
@jwt_required()
def protected():
    return ({'protected': 'protection'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)