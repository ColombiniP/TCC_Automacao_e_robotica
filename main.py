
import datetime
import streamlit as st
import Controllers.AlunoController as AlunosController
from models.Alunos import Alunos as alunos

st.set_page_config(page_title="CADASTRO DE ALUNO",page_icon="📚")

st.title('📚 Cadastro do aluno')

with st.form(key="Cadastro de aluno",clear_on_submit=True):
    input_nome = st.text_input(label="NOME")
    input_cpf = st.text_input("CPF")
    input_email = st.text_input(label="EMAIL")
    input_aniversario = st.date_input("DATA DE NASCIMENTO",format="DD.MM.YYYY",value=None,min_value=datetime.datetime.min)
    input_disciplina = st.selectbox("SELECIONE SEU CURSO",("Robótica e automação MD01","Robótica e automação MD02","Robótica e automação MD03"),index=None,placeholder="Escolha uma opção")
    input_btn = st.form_submit_button("Enviar", width="stretch")

if input_btn:
    alunos = alunos(input_nome,input_cpf,input_email,input_aniversario,input_disciplina)
    alunos.nome = input_nome
    alunos.cpf = input_cpf
    alunos.email = input_email
    alunos.aniversario = input_aniversario
    alunos.disciplina = input_disciplina
    AlunosController.cadastrarAlunos(alunos)
    