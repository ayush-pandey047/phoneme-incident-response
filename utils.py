import os

def load_logs() -> str:
    """Reads all log files from the logs directory and returns them as a single string."""
    log_dir = "logs"
    logs_content = ""
    
    # Specific files to read
    files_to_read = ["app-error.log", "nginx-access.log", "nginx-error.log"]
    
    for filename in files_to_read:
        filepath = os.path.join(log_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                logs_content += f"\n--- {filename} ---\n"
                logs_content += f.read()
        else:
            print(f"Warning: {filename} not found in {log_dir}")
            
    return logs_content
