from flask import Flask, render_template, send_from_directory, request, jsonify, make_response, url_for, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_conta')
def criar_conta():
    return render_template('criar_conta.html')

@app.route('/criar_conta_redirect', methods=['POST'])
def criar_conta_redirect():
    return redirect(url_for('criar_conta'))

if __name__ == '__main__':
    app.run(debug=True)

#
# tela login ----------------------------------------------------------------#
    
def login():
        username = request.form['username']
        password = request.form['password']
        print(f'Usuário: {username}, Senha: {password}')
        return redirect(url_for('/index'))
    
 # tela cadastro ----------------------------------------------------------------#
 
def cadastro():
        username = request.form['username']
        password = request.form['password']
        idade = request.form['idade']
        english = request.form['english']
        print(f'Usuário: {username}, Senha: {password}, idade :{idade}, {english}')
        
        return redirect(url_for('/criar_conta'))