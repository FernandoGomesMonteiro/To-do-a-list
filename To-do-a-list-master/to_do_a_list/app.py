from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'jack'

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

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = validate_login(username, password)
    if user:
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        flash('Senha errada')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        tasks = cursor.execute('SELECT * FROM tasks WHERE completed = 0').fetchall()
        completed_tasks = cursor.execute('SELECT * FROM tasks WHERE completed = 1').fetchall()
        conn.close()
        return render_template('dashboard.html', username=username, tasks=tasks, completed_tasks=completed_tasks)
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/adicionarinfo', methods=['POST'])
def adicionarinfo():
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    priority = request.form['priority']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description, due_date, priority, completed) VALUES (?, ?, ?, ?, ?)',
                   (title, description, due_date, priority, 0))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/editarinfo/<int:id>', methods=['GET', 'POST'])
def editinfo(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        cursor.execute('UPDATE tasks SET title = ?, description = ?, due_date = ?, priority = ? WHERE id = ?',
                       (title, description, due_date, priority, id))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    task = cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('editinfo.html', task=task)

@app.route('/completar/<int:id>')
def complete(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)