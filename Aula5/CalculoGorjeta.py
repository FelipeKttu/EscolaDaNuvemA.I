def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

  if valor_conta < 0 or porcentagem_gorjeta < 0:
    return 0.0
  gorjeta = (valor_conta * porcentagem_gorjeta) / 100
  return gorjeta


valor_da_conta = 240.50
percentual = 23
valor_da_gorjeta = calcular_gorjeta(valor_da_conta, percentual)

print(f"Conta: R$ {valor_da_conta:.2f}")
print(f"Gorjeta ({percentual}%): R$ {valor_da_gorjeta:.2f}")
print(f"Valor Total: R$ {(valor_da_conta + valor_da_gorjeta):.2f}")