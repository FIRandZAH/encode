# mau ngapain mau recode?
# yahh sorry ga bisa
# salam dari firman 😎
import os
import subprocess
import sys
def check_python_version():
    try:
        subprocess.run(['python', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return 'python'
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    try:
        subprocess.run(['python3', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return 'python3'
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    print("Python atau Python3 tidak ditemukan di sistem.")
    sys.exit(1)
def run_script(script_path, python_executable):
    subprocess.run([python_executable, script_path], check=True)
def main():
    os.system('git pull')
    python_executable = check_python_version()
    script_path = 'asu.py'
    run_script(script_path, python_executable)
if __name__ == "__main__":
    main()
