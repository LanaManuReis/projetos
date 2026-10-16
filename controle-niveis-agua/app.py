
from colorama import Fore, Style, init

# Inicialização da biblioteca
init(autoreset=True, strip=False)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (Crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (Alerta)"
]

# Função para definir a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibição dos níveis do reservatório
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)
