from cliente import Cliente
from conta import Conta

maico = Cliente('Maico', 232323232)
contaMaico = Conta(maico)

daniel = Cliente('Daniel', 757575757)
contaDaniel = Conta(daniel)

contaMaico.depositar(1000)
print('Saldo Maico: ' + str(contaMaico.saldo))

contaMaico.transferir(contaDaniel, 5000)

print('Saldo Daniel: ' + str(contaDaniel.saldo))
print('Novo saldo Maico: ' + str(contaMaico.saldo))
