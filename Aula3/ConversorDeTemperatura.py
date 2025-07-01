
def converter_temperatura():
    try:
        valor_str = input("Digite o valor da temperatura: ")
        valor = float(valor_str.replace(',', '.'))

        unidade_origem = input("Qual a unidade de origem (C, F, ou K)? ").upper()
        unidade_destino = input("Para qual unidade deseja converter (C, F, ou K)? ").upper()

        unidades_validas = ['C', 'F', 'K']
        if unidade_origem not in unidades_validas or unidade_destino not in unidades_validas:
            print("Erro: Unidade inválida. Por favor, use 'C', 'F' ou 'K'.")
            return


        if unidade_origem == 'F':
            temp_em_celsius = (valor - 32) * 5 / 9
        elif unidade_origem == 'K':
            temp_em_celsius = valor - 273.15
        else:
            temp_em_celsius = valor

        if unidade_destino == 'C':
            resultado_final = temp_em_celsius
        elif unidade_destino == 'F':
            resultado_final = (temp_em_celsius * 9 / 5) + 32
        else: # Se o destino é Kelvin
            resultado_final = temp_em_celsius + 273.15

        print("\n--- Resultado da Conversão ---")
        print(f"{valor:.2f}°{unidade_origem} é equivalente a {resultado_final:.2f}°{unidade_destino}.")

    except ValueError:
        print("Erro: Valor da temperatura inválido. Por favor, digite apenas números.")

converter_temperatura()