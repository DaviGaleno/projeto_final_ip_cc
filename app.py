import csv
from flask import Flask, render_template, jsonify, request, url_for, redirect
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key="AIzaSyDeY_wq649r9jzboYnDda-_KwL18lV56Bk")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("mensagem")

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(["Você é um professor de python que tira duvidas sobre assuntos de python, dando respostas curtas e diretas.",
        user_input
        ])
        resposta_bot = response.text
        print(response.text)
        resposta_bot = response.text
    except Exception as e:
        resposta_bot = f"[Erro]: {str(e)}"

    return jsonify({"resposta": resposta_bot})

@app.route('/vetoresematrizes')
def vetoresematrizes():
    return render_template('vetoresematrizes.html')

@app.route('/estruturasdeseleção')
def estruturasdeseleção():
    return render_template('estruturasdeseleção.html')


@app.route('/estruturasderepetição')
def estruturasderepetição():
    return render_template('estruturasderepetição.html')

@app.route('/dicionario')
def dicionario():

    dicionario_de_termos = []

    with open('bd_dicionario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for t in reader:
            dicionario_de_termos.append(t)

    return render_template('dicionario.html', dicionario=dicionario_de_termos)



@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')


@app.route('/criar_termo', methods=['POST'])
def criar_termo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_dicionario.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('dicionario'))

@app.route('/deletar_termo/<termo>')
def deletar_termo(termo):
    novos_termos = []

    with open('bd_dicionario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for t in reader:
            if t[0] != termo:
                novos_termos.append(t)

    with open('bd_dicionario.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(novos_termos)

    return redirect(url_for('dicionario'))

@app.route('/editar_termo/<termo>')
def editar_termo(termo):
    termo_encontrado = None

    with open('bd_dicionario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for t in reader:
            if t[0] == termo:
                termo_encontrado = t
                break

    if termo_encontrado:
        return render_template('editar_termo.html', termo=termo_encontrado)
    else:
        return redirect(url_for('dicionario'))


@app.route('/salvar_edicao', methods=['POST'])
def salvar_edicao():
    termo_original = request.form['termo_original']
    novo_termo = request.form['termo']
    nova_definicao = request.form['definicao']

    termos_atualizados = []

    with open('bd_dicionario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for t in reader:
            if t[0] == termo_original:
                termos_atualizados.append([novo_termo, nova_definicao])
            else:
                termos_atualizados.append(t)

    with open('bd_dicionario.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerows(termos_atualizados)

    return redirect(url_for('dicionario'))

app.run(debug=True)



