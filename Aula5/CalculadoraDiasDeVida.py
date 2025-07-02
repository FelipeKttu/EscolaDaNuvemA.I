from datetime import datetime

def calcular_dias_vividos():

  while True:
    data_nascimento_str = input("Digite sua data de nascimento (no formato DD/MM/AAAA): ")
    try:
      data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

      data_hoje = datetime.now()

      if data_nascimento > data_hoje:
          print("Erro: A data de nascimento não pode ser uma data futura.")
          continue # Pede a data novamente

      diferenca = data_hoje - data_nascimento

      print(f"\nAté a data de hoje ({data_hoje.strftime('%d/%m/%Y')}), você já viveu {diferenca.days} dias.")
      break
    except ValueError:
      print("Erro: Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")

calcular_dias_vividos()