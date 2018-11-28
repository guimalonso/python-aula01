from flask import Blueprint, render_template, request, redirect

view = Blueprint('view', __name__, url_prefix='/view')

@view.route('/')
def modelo_view():
    letras = [chr(x) for x in range(97, 123)]
    return render_template('index.html', letras=letras)

@view.route('/login')
def render_login():
    return render_template('login.html')

@view.route('/login', methods=['POST'])
def auth_login():
    auth = request.form
    if auth['login'].strip().lower() == 'teste' and auth['password'].strip().lower() == '123':
        retorno = {"auth": True}
    else:
        retorno = {"auth": False}
    return render_template('login.html', auth=retorno)