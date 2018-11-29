from flask import Blueprint, jsonify
from connect import mongo_connect

db = mongo_connect('test')
usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario.route('/')
def get_users():
    return jsonify(list(db.usuario.find()))

@usuario.route('/<string:user>')
def get_user(user):
    if user.isnumeric():
        try:
            return jsonify(db.usuario.find_one({"_id":int(user)}))
        except Exception:
            return None
    elif len(user.split('.')) == 3:
        return jsonify(db.usuario.find_one({"cpf":user}))
    else:
        return jsonify(list(db.usuario.find({"nome":user})))