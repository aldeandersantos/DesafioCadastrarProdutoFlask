from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        disponivel = bool(request.form.get('disponivel'))

        produtos.append({'nome': nome, 'descricao': descricao, 'valor': valor, 'disponivel': disponivel})
        
        return redirect(url_for('index'))

    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)