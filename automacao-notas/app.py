
# ==========================================
# ENTRADA
# ==========================================

def solicitar_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")

        except ValueError:
            print("Entrada inválida! Digite um número.")


def entrada_dados():
    nome = input("Nome do aluno: ")
    nota1 = solicitar_nota(1)
    nota2 = solicitar_nota(2)

    return nome, nota1, nota2


# ==========================================
# PROCESSAMENTO
# ==========================================

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def verificar_situacao(media):
    if media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


# ==========================================
# SAÍDA
# ==========================================

def gerar_relatorio(nome, media, situacao):
    print("\n--- RELATÓRIO DE DESEMPENHO ---")
    print(f"Aluno: {nome}")
    print(f"Média final: {media:.1f}")
    print(f"Situação: {situacao}")
    print("-" * 32)


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    try:
        quantidade = int(input("Quantos alunos deseja cadastrar? "))

        while quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            quantidade = int(input("Quantos alunos deseja cadastrar? "))

    except ValueError:
        print("Digite uma quantidade inteira válida.")
        return

    for i in range(quantidade):
        print(f"\nCadastro do aluno {i + 1}")

        # ENTRADA
        nome, nota1, nota2 = entrada_dados()

        # PROCESSAMENTO
        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)

        # SAÍDA
        gerar_relatorio(nome, media, situacao)


if __name__ == "__main__":
    main()