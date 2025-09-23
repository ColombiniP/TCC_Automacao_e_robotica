import services.database as db

def conexao():
    return db.connection


def cadastrarAlunos(Alunos):
    conn = conexao()
    cur = conn
    cur.execute("INSERT INTO Alunos(nome, cpf, email, aniversario, consentimento, disciplina) VALUES (?,?,?,?,?,?)",
                (Alunos.nome,Alunos.cpf,Alunos.email,Alunos.aniversario,Alunos.consentimento,Alunos.disciplina))
    conn.commit()
    conn.close()

def listarAlunos():
    conn = conexao()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Alunos")
    dados = cur.fetchall()
    cur.close()
    return dados