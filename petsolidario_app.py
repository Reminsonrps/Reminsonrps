from flask import Flask, render_template_string, request
from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()  # Carrega as variáveis do .env

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}


app = Flask(__name__)



form_html = """
<!DOCTYPE html>
<html lang='pt-br'>
<head>
    <meta charset='UTF-8'>
    <title>Formulário PetSolidário</title>
</head>
<body>
    <h1>📝 Descrição</h1>
    <p>Olá! Este formulário faz parte do projeto PetSolidário...</p>
    <form method='post'>
        <label>Nome completo:<br><input type='text' name='nome_completo'></label><br><br>
        <label>Bairro onde mora:<br><input type='text' name='bairro'></label><br><br>
        <label>Você já viu ou encontrou animais abandonados?<br>
            <select name='animais_abandonados'>
                <option>Sim</option>
                <option>Não</option>
            </select>
        </label><br><br>
        <label>Você estaria disposto(a) a divulgar pets?<br>
            <select name='divulgar_pets'>
                <option>Sim</option>
                <option>Não</option>
                <option>Talvez</option>
            </select>
        </label><br><br>
        <label>Já ajudou algum animal de rua?<br>
            <select name='ajudou_animais'>
                <option>Sim</option>
                <option>Não</option>
            </select>
        </label><br><br>
        <label>Conhece ONGs ou pessoas que ajudam?<br>
            <select name='conhece_ajuda'>
                <option>Sim</option>
                <option>Não</option>
            </select>
        </label><br><br>
        <label>Se sim, indique nome ou contato:<br>
            <textarea name='indicacoes' rows='4' cols='50'></textarea>
        </label><br><br>
        <label>Quais funções você considera úteis?<br>
            <input type='checkbox' name='funcoes' value='Publicar pets perdidos/encontrados'> Publicar pets perdidos/encontrados<br>
            <input type='checkbox' name='funcoes' value='Galeria de adoção responsável'> Galeria de adoção responsável<br>
            <input type='checkbox' name='funcoes' value='Dicas de cuidados, vacinação e castração'> Dicas de cuidados, vacinação e castração<br>
            <input type='checkbox' name='funcoes' value='Contato com ONGs e voluntários'> Contato com ONGs e voluntários<br>
            <input type='checkbox' name='funcoes' value='Denúncia de maus-tratos'> Denúncia de maus-tratos<br>
            <input type='checkbox' name='funcoes' value='Outro'> Outro (campo aberto)<br>
        </label><br><br>
        <label>O que você gostaria de ver no site?<br>
            <textarea name='sugestoes' rows='4' cols='50'></textarea>
        </label><br><br>
        <label>Tem alguma história com animais?<br>
            <textarea name='historia' rows='4' cols='50'></textarea>
        </label><br><br>
        <label>E-mail ou telefone:<br><input type='text' name='contato'></label><br><br>
        <label>Gostaria de ser voluntário(a)?<br>
            <select name='voluntario'>
                <option>Sim</option>
                <option>Não</option>
                <option>Talvez</option>
            </select>
        </label><br><br>
        <input type='submit' value='Enviar'>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        dados = {
            'nome_completo': request.form.get('nome_completo'),
            'bairro': request.form.get('bairro'),
            'animais_abandonados': request.form.get('animais_abandonados'),
            'divulgar_pets': request.form.get('divulgar_pets'),
            'ajudou_animais': request.form.get('ajudou_animais'),
            'conhece_ajuda': request.form.get('conhece_ajuda'),
            'indicacoes': request.form.get('indicacoes'),
            'funcoes': request.form.getlist('funcoes'),
            'sugestoes': request.form.get('sugestoes'),
            'historia': request.form.get('historia'),
            'contato': request.form.get('contato'),
            'voluntario': request.form.get('voluntario')
        }

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO respostas (
                nome_completo, bairro, animais_abandonados, divulgar_pets,
                ajudou_animais, conhece_ajuda, indicacoes, funcoes,
                sugestoes, historia, contato, voluntario
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                dados['nome_completo'], dados['bairro'], dados['animais_abandonados'], dados['divulgar_pets'],
                dados['ajudou_animais'], dados['conhece_ajuda'], dados['indicacoes'], ', '.join(dados['funcoes']),
                dados['sugestoes'], dados['historia'], dados['contato'], dados['voluntario']
            )
        )
        conn.commit()
        cursor.close()
        conn.close()

        return "Formulário enviado com sucesso! Obrigado por participar do PetSolidário. 🐾"
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(debug=True)
