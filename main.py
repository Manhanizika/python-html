from flask import Flask, render_template, request, url_for, flash, redirect

import forms
import use_cases
from database import db
from model import Cartao, Compra
from datetime import datetime
import os
import datetime

app = Flask(__name__, static_url_path='/static')

app.secret_key = b'd3fcbe64-7150-11ee-b1fe-93b6661203c1'

# Configura banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('JTECH_MYSQL_USER', 'root')}:{os.getenv('JTECH_MYSQL_PASSWORD', 'password')}@{os.getenv('JTECH_MYSQL_HOST', 'localhost')}:{os.getenv('JTECH_MYSQL_PORT', '3306')}/{os.getenv('JTECH_MYSQL_DATABASE', 'byte_card')}"
# 'mysql+mysqlconnector://root:password@localhost:3306/byte_card'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/cadastrarcartao', methods=['POST'])
def cadastra_cartao():
    form = forms.CadastraCartaoForm(request.form)
    if form.validate():
        if(form.id.data):
            use_cases.define_limite_nome(form.id.data, form.limite.data, form.cliente.data)
            flash('Dados do cartão alterado com sucesso.', 'info')
        else:
            use_cases.cadastra_cartao(form.cliente.data, form.limite.data)
            flash('Cartão cadastrado com sucesso.', 'info')
    return formulario_cartao()

@app.route('/listacartao', methods=['GET'])
def formulario_cartao(form=None) :
    # return render_template('listacartao.html', form = form, lista = use_cases.lista_cartoes())
    cartoes = []
    cartoes.append(Cartao(numero=123, validade='12/2023',  cvv=312, limite=334.31, cliente='Wiu'))
    cartoes.append(Cartao(numero=123, validade='12/2023',  cvv=312, limite=334.31, cliente='Wiu'))
    cartoes.append(Cartao(numero=123, validade='12/2023',  cvv=115, limite=4000.00, cliente='jorge'))
    cartoes.append(Cartao(numero=123, validade='12/2023',  cvv=312, limite=334.31, cliente='Wiu'))

    return render_template('listacartao.html', form = form, lista = cartoes)

@app.route('/cadastrocartao')
def cadastro_cartao(cartao = Cartao(id = 0, cliente = '', limite = 0)):
    return render_template('cadastrocartao.html', cartao = cartao)

@app.route('/cancelarcartao')
def cancela_cartao():
    id = request.args.get('id')
    use_cases.cancela_cartao(id)
    return formulario_cartao(request.form)

@app.route('/ativarcartao')
def ativa_cartao():
    id = request.args.get('id')
    use_cases.ativa_cartao(id)
    return formulario_cartao(request.form)

@app.route('/limitecartao')
def formulario_limite():
    id = request.args.get('id')
    cartao = use_cases.pesquisa_cartao_por_id(id)
    return cadastro_cartao(cartao)

@app.route('/cadastracompras')
def cadastrarCompras():
    return render_template('cadastracompras.html')


@app.route('/listacartao')
def listacartao():
    return render_template('listacartao.html')


@app.route('/relatoriodegastos')
def relatoriodegastos():

    #Tentei criar uma lista para relatório de gastos aqui, porém eu não consegui.

    #gastos.append({'id': 1547157415784198, "valor": 845.84, 'data': datetime.datetime.now(), 'categoria': "Lazer"})
    #gastos.append({'id': 4358648774188745, "valor": 2300.61, 'data': datetime.datetime.now(), 'categoria': "Alimentacao"})
    return render_template('relatorioDeGastos.html') #, lista = gastos)


@app.route('/visualizarfatura')
def visualizarFatura():
    # return render_template('visualizarFatura.html', lista = use_cases.listar_compras(1))
    compras = []
    #   id: Mapped[int] = mapped_column(primary_key=True)
    # valor: Mapped[float] = mapped_column(Numeric(precision=15,
    #                                              scale=2))
    # data: Mapped[datetime] = mapped_column(DateTime())
    # estabelecimento: Mapped[str] = mapped_column(String(1000))
    # categoria: Mapped[str] = mapped_column(String(255))
    # cartao_id: Mapped[int] = mapped_column(ForeignKey("cartoes.id"))
    # cartao: Mapped['Cartao'] = relationship()
    compras.append({'id': 123, "valor": 345.12, 'data': datetime.datetime.now(), 'estabelecimento': "Carrefour"})
    compras.append({'id': 43, "valor": 1000.10, 'data': datetime.datetime.now(), 'estabelecimento': "Liberdade"})
    return render_template('visualizarFatura.html', lista = compras)

@app.route('/dashboardhome')
def dashboardHome():
    return render_template('dashboardhome.html')


@app.route('/alterarlimite')
def alterarlimite():
    return render_template('alterarLimite.html')

if __name__ == '__main__':
    app.run(debug=True)
