from veiculo import Veiculo

veiculo = Veiculo('rosa', 6, 'uno', 40)

print(veiculo)
print(type(veiculo))

print('cor:', veiculo.cor)
print('roda:', veiculo.roda) 
print('marca:', veiculo.marca)
print('abastecer:', veiculo.tanque)
veiculo.abatecer(60)
print('abastecer:', veiculo.tanque)
