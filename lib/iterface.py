def clear_terminal():
    print('\033[H\033[2J', end='')

def main_menu():
    print("--- LOG ANALYZER ---")
    print("1. Exibir log completo")
    print("2. Exibir erros mais recentes")
    print("3. Filtrar mensagens")
    print("4. Pesquisar")
    print("5. Gerar relatório")
    print("0. Sair")
    opt = input("> ")

    return opt

def filter_menu():
    print("Por qual categoria deseja filtrar:")
    print("1. INFO")
    print("2. WARNING")
    print("3. ERROR")
    opt = input("> ")

    return opt