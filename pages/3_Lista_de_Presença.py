import streamlit as st
import datetime 

# st.title('Cadastro do aluno',)

# with st.form(key="Cadastro de aluno",clear_on_submit=True):
#     input_name = st.text_input(label="NOME")
#     input_last_name = st.text_input(label="SOBRENOME")
#     input_cpf = st.text_input("CPF")
#     input_email = st.text_input(label="EMAIL")
#     input_birth_day = st.date_input("DATA DE NASCIMENTO",format="DD.MM.YYYY",value=None,min_value=datetime.datetime.min)
#     input_disciplina = st.selectbox("SELECIONE SEU CURSO",("Robótica e automação MD01","Robótica e automação MD02","Robótica e automação MD03"),index=None,placeholder="Escolha uma opção")
#     st.form_submit_button("Enviar", width="stretch")

st.set_page_config(page_title="LISTA DE PRESENÇA",page_icon="📄")

st.write("""
# 📄 Lista de Presença
""")

# st.sidebar.success("PÁGINAS DE NAVEGAÇÃO")