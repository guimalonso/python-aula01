from flask import Blueprint, render_template, request, redirect
from connect import psy_connect

view = Blueprint('view', __name__, url_prefix='/view')
cur = psy_connect('python', '4linux', 'fundamentals')

@view.route('/')
def modelo_view():
    cur.execute("select * from usuario;")
    return render_template('index.html', usuarios=cur.fetchall())

@view.route('/<string:nome>')
def view_users(nome):
    cur.execute("select * from usuario where nome like '%{}%'".format(nome.title()))
    return render_template('index.html', usuarios=cur.fetchall())

# @view.route('/login')
# def render_login():
#     return render_template('login.html')

# @view.route('/login', methods=['POST'])
# def auth_login():
#     auth = request.form
#     if auth['login'].strip().lower() == 'teste' and auth['password'].strip().lower() == '123':
#         retorno = {"auth": True}
#     else:
#         retorno = {"auth": False}
#     return render_template('login.html', auth=retorno)