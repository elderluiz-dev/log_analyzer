def show_log(incoming_logs):
    logs = incoming_logs.splitlines() 
    for log in logs:
        print(f"{log}")
    print("\n")

def log_infos(incoming_logs):
    print("Detalhes do log selecionado:")
    logs = incoming_logs.splitlines()

    war = 0
    info = 0
    err = 0

    for log in logs:
        if "WARNING" in log:
            war += 1
        if "INFO" in log:
            info += 1
        if "ERROR" in log:
            err += 1
    
    infos = [war, info, err]

    return infos