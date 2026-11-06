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

def filter_menu():
    print("Por qual categoria deseja filtrar:")
    print("1. INFO")
    print("2. WARNING")
    print("3. ERROR")
    opt = input("> ")

    return opt