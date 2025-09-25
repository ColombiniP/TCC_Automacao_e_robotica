import datetime
import streamlit as st
import Controllers.AlunoController as AlunosController
from models.Alunos import Alunos as alunos
from models.Modulo import Modulo as md

st.set_page_config(page_title="CADASTRO DE ALUNO",page_icon="📚")

st.title('📚 Cadastro do aluno')

with st.form(key="Cadastro de aluno",clear_on_submit=True):
    input_nome = st.text_input(label="NOME")
    input_cpf = st.text_input("CPF",max_chars=11)
    input_email = st.text_input(label="EMAIL")
    input_data_nascimento = st.date_input("DATA DE NASCIMENTO",format="DD.MM.YYYY",value=None,min_value=datetime.datetime.min)
    input_disciplina = st.selectbox("SELECIONE SEU CURSO",("Robótica e automação MD01","Robótica e automação MD02","Robótica e automação MD03"),index=None,placeholder="Escolha uma opção")
    st.markdown("[CONSENTIMENTO DE USO DE DADOS](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)")
    input_check_lgpd = st.checkbox("",value=True)
    input_btn = st.form_submit_button("Enviar", width="stretch",disabled=False)
 
alunos = alunos(input_nome,input_cpf,input_email,input_data_nascimento,input_check_lgpd)
md = md(input_disciplina)

if input_btn:
    alunos.nome = input_nome
    alunos.cpf = input_cpf
    alunos.email = input_email
    alunos.data_nascimento = input_data_nascimento
    alunos.termo_consentimento_uso_dados_pessoais = input_check_lgpd
    md.disciplina = input_disciplina
    AlunosController.cadastrarAlunos(alunos)
    