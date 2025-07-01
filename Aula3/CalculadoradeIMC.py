
try:
    peso_str = input("Digite seu peso em kg: ")
    peso = float(peso_str.replace(',', '.'))

    altura_str = input("Digite sua altura em metros (ex: 1.75): ")
    altura = float(altura_str.replace(',', '.'))

    if peso <= 0 or altura <= 0:
        print("Erro: O peso e a altura devem ser valores positivos.")
    else:
        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"

        print("\n--- Resultado do seu IMC ---")
        print(f"Seu IMC é: {imc:.2f}") # Formata o IMC para ter apenas 2 casas decimais
        print(f"Classificação: {classificacao}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números para peso e altura.")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")