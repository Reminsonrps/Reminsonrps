from flask import Flask, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:van002@localhost/cadastro_db'
db = SQLAlchemy(app)

# Modelo da tabela
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100))
    email = db.Column(db.String(120))

# Cria o banco de dados
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']

    if not nome or not sobrenome or not email:
        return 'Todos os campos são obrigatórios.', 400

    try:
        novo_usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email)
        db.session.add(novo_usuario)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f'Erro ao salvar: {e}', 500

    return f'Cadastro salvo no banco: {nome} {sobrenome} ({email})'

@app.route('/exportar_csv')
def exportar_csv():
    usuarios = Usuario.query.all()

    def gerar():
        yield 'id,nome,sobrenome,email\n'
        for u in usuarios:
            yield f'{u.id},{u.nome},{u.sobrenome},{u.email}\n'

    return Response(gerar(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment;filename=usuarios.csv"})

if __name__ == '__main__':
    app.run(debug=True)
