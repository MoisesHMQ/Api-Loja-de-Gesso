from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

ferramentas_gesso = []
serviços = []
cliente = []


@app.route("/ferramentas", methods=['POST'])
def ferramentas():
    objetos = request.json
    for objetos_gesso in ferramentas_gesso:
        if objetos_gesso["ferramentas"] == objetos["ferramentas"]:
            return {"status": "Produto já cadastrado."}
    objetos = {
        "id": str(uuid.uuid4()),
        "ferramentas": objetos["ferramentas"]
    }
    ferramentas_gesso.append(objetos)
    return jsonify(objetos)


@app.route("/estoque/ferramentas")
def estoque():
    return jsonify(ferramentas_gesso)


@app.route("/deletar/ferramentas", methods=['POST'])
def excluir():
    excluir_ferramentas = request.json
    print(ferramentas_gesso)
    for deletar_ferramentas in ferramentas_gesso:
        if deletar_ferramentas["id"] == excluir_ferramentas["id"]:
            ferramentas_gesso.remove(deletar_ferramentas)
            return excluir_ferramentas


@app.route("/serviços", methods=['POST'])
def cadastrar():
    obras = request.json
    for user in serviços:
        if user["nºcontrato"] == obras["nºcontrato"]:
            return {"erro.": "nºcontrato em processo."}
    obras = {
        "id": str(uuid.uuid4()),
        "nºcontrato": obras["nºcontrato"],
        "senha": obras["senha"]
    }
    serviços.append(obras)
    return jsonify(obras)


@app.route("/login/serviços", methods=['POST'])
def logar():
    banco_de_dados = request.json
    for login in serviços:
        if login["nºcontrato"] == banco_de_dados["nºcontrato"] and login["senha"] == banco_de_dados["senha"]:
            return{"Status": "contrato ativo."}
        else:
            return{"Status": "nºcontrato ou senha incorreto."}


@app.route("/construções/ativas")
def listar_serviços():
    return jsonify(serviços)


@app.route("/excluir/serviços", methods=['POST'])
def excluir_usuarios():
    termino_e_exclusão = request.json
    print(serviços)
    for dell in serviços:
        if dell["id"] == termino_e_exclusão["id"]:
            serviços.remove(dell)
            return termino_e_exclusão


@app.route("/cadastrar/clientes", methods=['POST'])
def cadastro_clientes():
    cad = request.json
    for user in cad:
        if user["login"] == cad["login"]:
            return {"Algo deu errado.": "Esse usuario ja existe."}
    cad = {
        "id": str(uuid.uuid4()),
        "login": cad["login"],
        "senha": cad["senha"]
    }
    cliente.append(cliente)
    return jsonify(cliente)


@app.route("/login/clientes", methods=['POST'])
def entrar():
    logar = request.json
    for login in cliente:
        if login["login"] == logar["login"] and login["senha"] == logar["senha"]:
            return{"Status": "Logado."}
        else:
            return{"Status": "Usuario ou Senha Incorretos."}


@app.route("/usuarios/ativos")
def listar_usuarios():
    return jsonify(cliente)

@app.route("/excluir/clientes", methods=['POST'])
def delete_usuarios():
    delete = request.json
    print(cliente)
    for list in cliente:
        if list["id"] == delete["id"]:
            cliente.remove(list)
            return delete

app.run()

