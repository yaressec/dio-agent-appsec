"""Aplicação de laboratório INTENCIONALMENTE VULNERÁVEL.

Uso exclusivo para a aula de análise de vulnerabilidades. Não exponha.
Roda em banco SQLite em memória, sem rede, sem dados reais.
"""
import sqlite3


def conectar():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    )
    conn.execute(
        "INSERT INTO usuarios (username, password) VALUES (?, ?)",
        ("aluno", "senha123"),
    )
    conn.commit()
    return conn


def login(username, password):
    """VULNERÁVEL: concatena a entrada diretamente na instrução SQL."""
    conn = conectar()
    sql = (
        "SELECT id FROM usuarios "
        "WHERE username = '" + username + "' AND password = '" + password + "'"
    )
    cursor = conn.execute(sql)
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


if __name__ == "__main__":
    print("Login normal:", login("aluno", "senha123"))
    print("Login com senha errada:", login("aluno", "errada"))
