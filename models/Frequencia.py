import datetime

class Frequencia:

    def __init__(self, id, aluno_cpf, turma_id, data, presenca):
        if not isinstance(data,datetime.date):
            raise TypeError("O atributo 'data', deve ser do tipo datetime.date")
        
        if not isinstance(presenca,bool):
            raise TypeError("O atributo 'presenca', deve ser do tipo boolean")
        
        self.id = id
        self.aluno_cpf = aluno_cpf
        self.turma_id = turma_id
        self.data = data
        self.presenca = presenca