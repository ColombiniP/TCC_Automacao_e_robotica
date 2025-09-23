# RODAR A APLICAÇÃO

Para rodar a aplicação execue:

```bash
python -m streamlit run <main.py>
```

Página é executada no:  
http://localhost:8501/

## streamlit

- É a biblioteca escolhida pela facilidade de criar o front-end e os campos de formulários.

- [Referência](https://docs.streamlit.io/)

## SQLite3

Banco relacional local, escolhido por já ter os drivers e a sua api já serem nativas do python, e pela facilidade de lidar com as tabelas e cadastros e mostrar isso na tela do front-end

### Conexão do SQLite3

- Na pasta service, localizada na raiz do projeto, criamos o arquivo `database.py`.

- Importamos o sqlite3 que já é nativo do python
    ```py
        import sqlite3

        connect = sqlite3.connect("database.db")
        connect.cursor()  
    ```

- [Referência](https://docs.python.org/pt-br/3.13/library/sqlite3.html)