# 4- Calculadora de Consumo de Combustível

distancia_percorrida = 300  # em km
combustivel_gasto = 25    # em litros
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("\n### Calculadora de Consumo de Combustível ###")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("-" * 25)
print(f"Consumo Médio: {consumo_medio:.2f} km/l")