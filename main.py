from flask import Flask, render_template, request, url_for, flash, redirect

import forms
import use_cases
from database import db
from model import Cartao, Compra
from datetime import datetime
import os

app = Flask(__name__, static_url_path='/static')

app.secret_key = b'd3fcbe64-7150-11ee-b1fe-93b6661203c1'

# Configura banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('JTECH_MYSQL_USER', 'root')}:{os.getenv('JTECH_MYSQL_PASSWORD', 'password')}@{os.getenv('JTECH_MYSQL_HOST', 'localhost')}:{os.getenv('JTECH_MYSQL_PORT', '3306')}/{os.getenv('JTECH_MYSQL_DATABASE', 'byte_card')}"
# 'mysql+mysqlconnector://root:password@localhost:3306/byte_card'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

messages = [{'name': 'Message One',
             'content': 'Message One Content'},
            {'limit': 'Message Two',
             'content': 'Message Two Content'}
            ]

cartoes = []

@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/cadastrocartao', methods=('GET', 'POST'))
def cadastrarCartao():
    messages.clear()
    print(request.method)
    if request.method == 'POST':
        name = request.form['txtNome']
        limit = request.form['txtLimite']
        if not name:
            flash('Nome é obrigatório!')
        elif not limit:
            flash('Limite do cartão é obrigatório')
            messages.append({'name': name, 'limit': limit})
        else:
            flash(name + ' cadastrado com sucesso')
            cartoes.append({'name': name, 'limit': limit})

        messages.append({'name': name, 'limit': limit})
        listaCartoes = use_cases.lista_cartoes()
        return render_template('cadastrocartao.html', lista = listaCartoes, tamanhoLista = len(listaCartoes))
    else:
        listaCartoes = use_cases.lista_cartoes()
        return render_template('cadastrocartao.html',  lista = listaCartoes, tamanhoLista = len(listaCartoes))


@app.route('/cadastracompras')
def cadastrarCompras():
    return render_template('cadastracompras.html')


@app.route('/listacartao')
def listacartao():
    return render_template('listacartao.html')


@app.route('/relatoriodegastos')
def relatoriodegastos():
    return render_template('relatorioDeGastos.html')


@app.route('/visualizarfatura')
def visualizarFatura():
    return render_template('visualizarFatura.html')


@app.route('/dashboardhome')
def dashboardHome():
    return render_template('dashboardhome.html')


@app.route('/alterarlimite')
def alterarlimite():
    return render_template('alterarLimite.html')


if __name__ == '__main__':
    app.run(debug=True)
