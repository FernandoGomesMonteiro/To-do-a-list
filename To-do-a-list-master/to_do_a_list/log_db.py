import sqlite3

def setup_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Criação da tabela de usuários
    cursor.execute('''
    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    idade INTEGER
    );
    ''')

    # Criação da tabela de tarefas
    cursor.execute('''
    CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    priority TEXT,
    completed INTEGER NOT NULL DEFAULT 0
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()