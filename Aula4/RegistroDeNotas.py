def calcular_media_turma():
    notas = []
    while True:
        entrada_nota = input("Digite a nota do aluno (ou 'fim' para terminar): ")

        if entrada_nota.lower() == 'fim':
            break

        try:
            nota = float(entrada_nota)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if not notas:
        print("\nNenhuma nota foi inserida.")
        return

    media = sum(notas) / len(notas)

    print("\n--- Relatório da Turma ---")
    print(f"Total de notas registradas: {len(notas)}")
    print(f"As notas foram: {notas}")
    print(f"A média da turma é: {media:.2f}")

calcular_media_turma()