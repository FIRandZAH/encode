# mau ngapain mau recode?
# yahh sorry ga bisa
# salam dari firman 😎
import os
import subprocess
import sys
def check_python_version():
    python_available = subprocess.run(['which', 'python'], capture_output=True, text=True)
    if python_available.returncode == 0:
        return 'python'
    python3_available = subprocess.run(['which', 'python3'], capture_output=True, text=True)
    if python3_available.returncode == 0:
        return 'python3'
def run_script(script_path, python_executable):
    subprocess.run([python_executable, script_path], check=True)
def main():
    os.system('git pull')
    python_executable = check_python_version()
    script_path = 'asu.py'
    run_script(script_path, python_executable)
if __name__ == "__main__":
    main()
