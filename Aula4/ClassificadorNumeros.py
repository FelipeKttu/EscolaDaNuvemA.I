def classificar_numeros():

    contador_pares = 0
    contador_impares = 0

    print("Digite os números um por um. Digite 'parar' para finalizar.")

    while True:
        entrada = input("Digite um número: ")

        if entrada.lower() == 'parar':
            break

        try:
            numero = int(entrada)
            # Verifica se o número é par ou ímpar
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                contador_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                contador_impares += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'parar'.")

    # Exibe o resultado final
    print("\n--- Fim da Análise ---")
    print(f"Total de números PARES inseridos: {contador_pares}")
    print(f"Total de números ÍMPARES inseridos: {contador_impares}")

classificar_numeros()