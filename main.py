# criar uma API de livros 

# Get, Post, Put, Delete

#Get - Buscar os dados dos livros (Read)
# Post - Adicionar novos livros (Create)
# Put - Atualizar informações dos livros (Update)
# Delete - Deletar informações dos livros (Delete)

#CRUD
# CRUD - Create, Read, Update, Delete

from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from typing import Optional 

app = FastAPI()

meus_livros = {}

class Livro(BaseModel):
    nome_livro: str
    autor_livro: str
    ano_livro: int

@app.get("/livros")
def get_livros():
    if not meus_livros:
        return {"message": "Não existe nenhum livro!"}
    else:
        return {"livros": meus_livros}

# id do livro
# nome do livro
# autor do livro
# ano de lançamento do livro

@app.post("/adiciona")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meus_livros:
        raise HTTPException(status_code=400, detail="Esse livro já existe!")
    else: 
        meus_livros[id_livro] = livro.model_dump()
        return {"message": "O livro foi criado com sucesso!"}

# Biblioteca -> livro precisa ser atualizado
# 1. Quem é o livro? -> id_livro
# 2. Pegar o livro -> get id_livro
# 3. Atualizar informação do livro

@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livro: Livro):
    meu_livro = meus_livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else: 
        meu_livro[id_livro]=livro.model_dump()

        return {"message": "As informações do seu livro foram atualizadascom sucesso!"}

@app.delete("/deletar/{id_livro}")
def delete_livros(id_livro: int):
    if id_livro not in meus_livros:
        raise HTTPException(status_code=404, detail="Esse livro não foi encontrado!")
    else:
        del meus_livros[id_livro]
        return {"message": "Seu livro foi deletado com sucesso!"}


# Vamos acessar nosso ENDPOINT da API pelo servidor criado na máquina http://127.0.0.1:8000 no Insomnia para testar as operações CRUD.
# E vamos acessar os PATH's desse endpoint como 
# GET -> http://127.0.0.1:8000/livros
# POST -> http://127.0.0.1:8000/adiciona
# PUT -> http://127.0.0.1:8000/atualiza/{id_livro}
# DELETE -> http://127.0.0.1:8000/deletar/{id_livro}
