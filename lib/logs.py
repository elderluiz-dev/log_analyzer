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

def review_log(incoming_logs):
    logs = incoming_logs.splitlines()
    for index, log in enumerate(logs):
        if "INFO" in log or "WARNING" in log or "ERROR" in log:
            continue
        else:
            print(f"Linha {index + 1} inválida!")

        log_splited = log.split()
        if len(log_splited) < 3:
            print(f"Linha {index + 1} inválida!")
    
    print("\n")

def filter_by_info(incoming_logs):
    logs = incoming_logs.splitlines()
    for log in logs:
        if "INFO" in log:
            print(f"{log}")
    print("\n")

def filter_by_warn(incoming_logs):
    logs = incoming_logs.splitlines()
    for log in logs:
        if "WARNING" in log:
            print(f"{log}")
    print("\n")

def filter_by_err(incoming_logs):
    logs = incoming_logs.splitlines()
    for log in logs:
        if "ERROR" in log:
            print(f"{log}")    
    print("\n")

def generate_repot(incoming_logs):
    logs = incoming_logs.splitlines()

    war = 0
    info = 0
    err = 0
    
    for log in logs:
        if "INFO" in log:
            info += 1
        if "WARNING" in log:
            war += 1
        if "ERROR" in log:
            err += 1

    total = war + info + err

    output_path = Path(__file__).parent / ".." / "reports"
    output_file = Path(__file__).parent / ".." / "reports" / "report.txt"

    output_path.mkdir(parents=True, exist_ok=True)
    output_file.touch(exist_ok=True)

    with open(output_file, "w", encoding='utf-8') as file:
        file.write(f"Log Analyzer - Relatório\nTotal de ocorrências: {total}\n\n")
        file.write(f"Total de infos: {info}\nTotal de warnings: {war}\nTotal de erros: {err}\n")