from lib.iterface import *
from lib.logs import *
from lib.shows import *

def main():
    clear_terminal()

    selected_file = init_log()
    if selected_file == False:
        return

    with open(selected_file, "r") as file:
        logs = file.read()

    clear_terminal()
    while True:
        infos = log_infos(logs)
        print(f"INFOS: {infos[0]} | WARNINGS: {infos[1]} | ERRORS: {infos[2]}\n")

        opt = main_menu()
        match opt:
            case "1":
                clear_terminal()
                show_log(logs)
            case "0":
                clear_terminal()
                print("Programa ecerrado pelo usuário")
                break
            case _:
                clear_terminal()
                print("Opção inválida")

if __name__ == "__main__":
    main()