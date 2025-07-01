
try:
    ano_str = input("Digite um ano para verificar se é bissexto: ")
    ano = int(ano_str)

    if ano <= 0:
        print("Erro: Por favor, insira um ano válido (número positivo).")
    else:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f" O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")

except ValueError:
    print("Entrada inválida. Por favor, digite um ano usando apenas números (ex: 2024).")