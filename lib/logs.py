from pathlib import Path

def init_log():
    print("-- LOG ANALYZER ---")

    LOG_DIR = Path(__file__).parent / "../logs"
    files = [
        file for file in LOG_DIR.iterdir()
        if file.is_file and file.suffix == ".log"
    ]

    if files == []:
        print("Não há logs cadastrados.")
        return False

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.name}")
    print("\nSelecione um log para usar")
    opt = int(input("> "))

    if 1 <= opt <= len(files):
        selected_file = files[opt - 1]
    else:
        print("Opção inválida")
        return False

    return selected_file