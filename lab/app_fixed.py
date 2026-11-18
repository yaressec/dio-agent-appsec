"""Versão corrigida do laboratório — query parametrizada + hash com salt.

Mudanças em relação a app.py:
  1. os valores não são concatenados: viram parâmetros da query;
  2. a senha é armazenada como hash PBKDF2 com salt, nunca em texto puro;
  3. mensagens de erro não revelam detalhes do banco.
"""
import hashlib
import hmac
import os
import sqlite3

ITERACOES = 120_000


def hash_senha(senha: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    salt = salt or os.urandom(16)
    digest = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, ITERACOES)
    return salt, digest


def conectar():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, username TEXT, salt BLOB, senha_hash BLOB)"
    )
    salt, digest = hash_senha("senha123")
    conn.execute(
        "INSERT INTO usuarios (username, salt, senha_hash) VALUES (?, ?, ?)",
        ("aluno", salt, digest),
    )
    conn.commit()
    return conn


def login(username, password):
    """SEGURO: usa placeholders (?) — dados nunca viram código SQL."""
    conn = conectar()
    try:
        cursor = conn.execute(
            "SELECT id, salt, senha_hash FROM usuarios WHERE username = ?",
            (username,),
        )
        registro = cursor.fetchone()
        if registro is None:
            # Mesmo erro para usuário inexistente e senha errada.
            return False
        _, salt, esperado = registro
        _, calculado = hash_senha(password, salt)
        return hmac.compare_digest(esperado, calculado)
    finally:
        conn.close()


if __name__ == "__main__":
    print("Login normal:", login("aluno", "senha123"))
    print("Login com senha errada:", login("aluno", "errada"))
