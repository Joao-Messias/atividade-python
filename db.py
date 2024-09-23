import sqlite3
from pathlib import Path

DB_PATH = Path('data/livraria.db')

def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.isolation_level = None  # Usar commit automático
    return conn


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_livro(titulo, autor, ano_publicacao, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao, preco)
        VALUES (?, ?, ?, ?)
    ''', (titulo, autor, ano_publicacao, preco))
    conn.commit()
    conn.close()

def listar_livros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conn.close()
    return livros

def atualizar_preco(livro_id, novo_preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE livros SET preco = ? WHERE id = ?', (novo_preco, livro_id))
    conn.commit()
    conn.close()

def remover_livro(livro_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (livro_id,))
    conn.commit()
    conn.close()

def buscar_por_autor(autor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE autor LIKE ?', ('%' + autor + '%',))
    livros = cursor.fetchall()
    conn.close()
    return livros
