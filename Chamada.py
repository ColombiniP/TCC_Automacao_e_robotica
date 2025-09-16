import streamlit as st

st.set_page_config("CHAMADA",page_icon="🙋‍♂️")

st.title("🙋‍♂️ Chamada")

st.markdown(
    """
    - Chamada digital!

"""
)
name = st.text_input("NOME")
last_name = st.text_input("SOBRE-NOME")

if st.button("PRESENTE"):
    st.write(f'{name} {last_name}')
else: 
    st.dialog("Preencha os campos")

