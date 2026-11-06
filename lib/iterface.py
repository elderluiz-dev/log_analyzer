def clear_terminal():
    print('\033[H\033[2J', end='')

def main_menu():
    print("--- LOG ANALYZER ---")
    print("1. Exibir log completo")
    print("2. Filtrar mensagens")
    print("3. Pesquisar")
    print("4. Gerar relatório")
    opt = input("> ")

    return opt