from contador import obterNumeroConta
import json
import uuid

class Conta:
  def __init__(self, cliente):
    self.id = str(uuid.uuid4())
    self.cliente = cliente
    self.agencia = '0001'
    self.conta = obterNumeroConta()
    self.saldo = 0

  def transferir(self, contaDestino, valor):
    if valor > self.saldo:
      raise Exception('Saldo insuficiente.')

    if valor <= 0:
      raise Exception('Valor negativo nao permitido.')

    self.saldo -= valor
    contaDestino.saldo += valor

  def depositar(self, valor):
    if valor <= 0:
      raise Exception('Valor negativo nao permitido.')
    self.saldo += valor

  def __str__(self):
    return json.dumps(self, default=lambda o: o.__dict__,
      sort_keys=True, indent=4)
