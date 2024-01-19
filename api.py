import json
from flask import Flask, Response, request

from cliente import Cliente

maico = Cliente('Maico', 232323232)
daniel = Cliente('Daniel', 757575757)
clientes = [maico.__dict__, daniel.__dict__]

app = Flask(__name__)

@app.get('/clientes')
def obterClientes():
  return Response(json.dumps(clientes), mimetype="application/json")

@app.get('/clientes/<idCliente>')
def obterClientePorId(idCliente):
  for cliente in clientes:
    if cliente['id'] == idCliente:
      return Response(json.dumps(cliente), mimetype="application/json")

  return Response(None, status=404)

@app.post('/clientes')
def criarCliente():
  for cliente in clientes:
    if cliente['documento'] == request.get_json()['documento']:
      erro = {
        'mensagem': f'Cliente com documento {request.get_json()["documento"]} ja cadastrado.'
      }

      return Response(json.dumps(erro), mimetype="application/json", status=400)

  novoCliente = Cliente(
    request.get_json()['nome'],
    request.get_json()['documento']
  )
  clientes.append(novoCliente.__dict__)

  return Response(json.dumps(novoCliente.__dict__), mimetype="application/json", status=201)

app.run(host="0.0.0.0", port=5000)
