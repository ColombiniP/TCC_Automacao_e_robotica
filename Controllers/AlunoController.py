import services.database as db

def conexao():
    return db.conexao


def cadastrarAlunos(Alunos):
    conn = conexao()
    cur = conn
    cur.execute("INSERT INTO Alunos(nome, cpf, email, data_nascimento, termo_consentimento_uso_dados_pessoais) VALUES (?,?,?,?,?)",
                (Alunos.nome,Alunos.cpf,Alunos.email,Alunos.data_nascimento,Alunos.termo_consentimento_uso_dados_pessoais))
    conn.commit()
    conn.close()

def listarAlunos():
    conn = conexao()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Alunos")
    dados = cur.fetchall()
    cur.close()
    return dados