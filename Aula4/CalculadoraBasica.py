def calculadora(num1: float, num2: float, operador: str) -> str:

    if operador == '+':
        return f"Resultado: {num1 + num2}"
    elif operador == '-':
        return f"Resultado: {num1 - num2}"
    elif operador == '*':
        return f"Resultado: {num1 * num2}"
    elif operador == '/':
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        else:
            return f"Resultado: {num1 / num2}"
    else:
        return "Erro: Operador inválido. Use +, -, * ou /."

try:
    numero1 = float(input("Digite o primeiro número: "))
    operador_input = input("Digite a operação (+, -, *, /): ")
    numero2 = float(input("Digite o segundo número: "))

    print(calculadora(numero1, numero2, operador_input))

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas números.")