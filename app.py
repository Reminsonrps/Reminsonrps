from flask import Flask,request, render_template,make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:van002@localhost/cooperado'
db = SQLAlchemy(app)

class cooperado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    contato = db.Column(db.String(20))
    funcao = db.Column(db.String(100))


# Cria o banco e tabela
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('novo_cooperado.html')

@app.route('/coop', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    contato= request.form['contato']
    funcao= request.form['funcao']

    if not nome or not contato or not funcao :
        return 'Todos os campos são obrigatórios.', 400

    try:
        novo_cooperado = cooperado(nome=nome, contato=contato, funcao=funcao)
        db.session.add(novo_cooperado)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f'Erro ao salvar: {e}', 500

    return f'Cadastro salvo no banco: {nome} {contato} ({funcao})'

from flask import make_response

@app.route('/exportar_csv')
def exportar_csv():
    novo_cooperado = cooperado.query.all()

    def gerar():
        yield 'id,nome,contato,funcao\n'
        for u in novo_cooperado:
            yield f'{u.id},{u.nome},{u.contato},{u.funcao}\n'

    resposta = make_response(gerar())
    resposta.headers["Content-Type"] = "text/csv"
    resposta.headers["Content-Disposition"] = "attachment; filename=usuarios.csv"
    return resposta

if __name__ == '__main__':
    app.run(debug=True)

