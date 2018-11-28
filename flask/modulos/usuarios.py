from flask import Blueprint, jsonify

usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

users = [
    {'nome': 'teste1', 'idade': 18},
    {'nome': 'teste2', 'idade': 18},
    {'nome': 'teste3', 'idade': 18}
]

@usuario.route('/')
def get_usuarios():
    return jsonify(users)

@usuario.route('/<int:user>')
def get_user(user):
    return jsonify(users[user-1])