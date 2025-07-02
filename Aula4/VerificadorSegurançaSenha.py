def verificar_senha(senha: str):

    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    if not any(char.isdigit() for char in senha):
        erros.append("A senha deve conter pelo menos um número.")

    if not erros:
        print(" Senha válida e segura!")
    else:
        print(" Senha inválida. Motivos:")
        for erro in erros:
            print(f"- {erro}")

senha_usuario = input("Digite a senha desejada: ")
verificar_senha(senha_usuario)