def calcular_preco_final():

  try:
    preco_original_str = input("Digite o preço original do produto: R$ ")
    preco_original = float(preco_original_str.replace(',', '.'))

    percentual_desconto_str = input("Digite o percentual de desconto (ex: 15 para 15%): ")
    percentual_desconto = float(percentual_desconto_str.replace(',', '.'))

    if preco_original < 0 or percentual_desconto < 0:
        print("Erro: Os valores de preço e desconto não podem ser negativos.")
        return

    valor_do_desconto = (preco_original * percentual_desconto) / 100

    preco_final = preco_original - valor_do_desconto


    print("\n--- Resumo do Cálculo ---")
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto ({percentual_desconto}%): R$ -{valor_do_desconto:.2f}")
    print(f"Preço Final: R$ {preco_final:.2f}")

  except ValueError:
    print("\nErro: Entrada inválida. Por favor, digite apenas números.")
  except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")


calcular_preco_final()