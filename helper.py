import os
import subprocess

def is_ignored(path):
    if ".git" in path.split(os.sep):  # Explicitly ignore .git directory
        return True
    
    try:
        result = subprocess.run(
            ["git", "check-ignore", "-q", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except Exception:
        return False

def print_tree(startpath, indent=""):
    for item in os.listdir(startpath):
        path = os.path.join(startpath, item)
        
        if is_ignored(path):
            continue

        if os.path.isdir(path):
            print(f"{indent}📂 {item}")
            print_tree(path, indent + "  ")
        else:
            print(f"{indent}📄 {item}")

print_tree(".")  # Change "." to your project directory if needed.
