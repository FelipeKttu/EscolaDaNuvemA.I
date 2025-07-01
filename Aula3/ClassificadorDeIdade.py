try:
    idade_str = input("Digite sua idade: ")
    idade = int(idade_str)

    if idade < 0:
        print("Erro: A idade não pode ser um número negativo.")
    else:
        if idade <= 12:
            categoria = "Criança"
        elif idade <= 17:
            categoria = "Adolescente"
        elif idade <= 59:
            categoria = "Adulto"
        else:
            categoria = "Idoso"

        print(f"Com {idade} anos, você é classificado(a) como: {categoria}.")

except ValueError:
    print("Entrada inválida. Por favor, digite sua idade usando apenas números.")