import sqlite3

# with sqlite3.connect("services/alunos.db",check_same_thread=False) as connection:
#     cursor = connection.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Alunos (
#             ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#             nome TEXT NOT NULL,
#             cpf TEXT NOT NULL,
#             email TEXT NOT NULL,
#             aniversario DATE,
#             consentimento BOOLEAN NOT NULL,
#             disciplina TEXT NOT NULL)
#     """)
#     cursor.close()

with sqlite3.connect('services/frequencia.db',check_same_thread=False) as conexao:
    cursor = conexao.cursor()

    def criar_tabelas():

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Professores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Modulo(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                disciplina TEXT NOT NULL,
                professor_id INTEGER,
                FOREIGN KEY(professor_id) REFERENCES Professores(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Turma(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                modulo_id INTEGER,
                ativa BOOLEAN,
                periodo TEXT,
                FOREIGN KEY(modulo_id) REFERENCES Modulo(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alunos(
                cpf TEXT PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT,
                data_nascimento DATE,
                termo_consentimento_uso_dados_pessoais BOOLEAN
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alunos_Turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_cpf TEXT,
                turma_id INTEGER,
                FOREIGN KEY(aluno_cpf) REFERENCES Alunos(cpf),
                FOREIGN KEY(turma_id) REFERENCES Turma(id)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Frequencia(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_cpf TEXT,
                turma_id INTEGER,
                data DATE,
                presenca BOOLEAN,
                FOREIGN KEY(aluno_cpf) REFERENCES Alunos(cpf),
                FOREIGN KEY(turma_id) REFERENCES Turma(id)
            )
        ''')

        conexao.commit()

criar_tabelas()