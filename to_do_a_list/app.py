from flask import Flask, render_template, send_from_directory, request, jsonify, make_response, url_for, redirect, flash, session 
import sqlite3


app = Flask(__name__)
app.secret_key='jack'
def validate_login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_conta')
def criar_conta():
    return render_template('criar_conta.html')

@app.route('/criar_conta_redirect', methods=['POST'])
def criar_conta_redirect():
    return redirect(url_for('criar_conta'))


#
# tela cadastro ----------------------------------------------------------------#
@app.route('/criar_conta_db', methods=['POST'])
def criar_conta_db():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    idade = request.form['idade']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, email, idade) VALUES (?, ?, ?, ?)', 
                   (username, password, email, idade))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

    
    
 # tela login ----------------------------------------------------------------#
 
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = validate_login(username, password)
    if user :
        session['username'] = username
       
        return redirect (url_for('dashboard'))
    
    else:
        flash('senha errada')
        return redirect (url_for('index'))
    
    
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template ('dashboard.html', username=username)
    else:
        return redirect (url_for('index'))
    
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect (url_for('index'))
    
    
    
    
    
    
    
if __name__ == '__main__':
       app.run(debug=True)
    