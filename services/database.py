import sqlite3

with sqlite3.connect("services/alunos.db",check_same_thread=False) as connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Alunos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            email TEXT NOT NULL,
            aniversario DATE,
            consentimento BOOLEAN NOT NULL,
            disciplina TEXT NOT NULL)
    """)
    cursor.close()