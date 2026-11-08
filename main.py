from lib.iterface import *
from lib.logs import *
from lib.shows import *

def main():
    clear_terminal()

    log_file = init_log()
    if log_file == False:
        return

    with open(log_file, "r") as file:
        logs = file.read()

    clear_terminal()
    review_log(logs)
    while True:
        infos = log_infos(logs)
        print(f"INFOS: {infos[0]} | WARNINGS: {infos[1]} | ERRORS: {infos[2]}\n")

        opt = main_menu()
        match opt:
            case "1":
                clear_terminal()
                show_log(logs)


            case "2":
                clear_terminal()
                filter_by_err(logs)


            case "3":
                clear_terminal()
                opt = filter_menu()
                match opt:
                    case "1":
                        clear_terminal()
                        filter_by_info(logs)
                    case "2":
                        clear_terminal()
                        filter_by_warn(logs)
                    case "3":
                        clear_terminal()
                        filter_by_err(logs)


            case "4":
                clear_terminal()
                search = input("Digite a pesquisa: ")
                clear_terminal()
                search_in_logs(logs, search)


            case "5":
                clear_terminal()
                generate_repot(logs)
                print("Relatório gerado com sucesso!\n")
                

            case "0":
                clear_terminal()
                print("Programa ecerrado pelo usuário")
                break


            case _:
                clear_terminal()
                print("Opção inválida")

if __name__ == "__main__":
    main()