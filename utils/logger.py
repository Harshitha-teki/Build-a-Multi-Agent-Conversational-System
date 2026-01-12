import datetime

def log_event(agent_name, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{agent_name.upper()}] {message}"
    print(log_entry)
    
    # Save to a file to show work history
    with open("system_logs.txt", "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")