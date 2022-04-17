"""13. Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele."""

import subprocess

def create_external_process(process_name):
    """
    Create a new external process.
    """
    return subprocess.Popen(process_name, shell=True)

def print_process_info(process):
    """
    Print process info.
    """
    print('PID:', process.pid)

def main():
    """
    Main function.
    """
    process_name = input('Enter process name: ')
    process = create_external_process(process_name)
    print_process_info(process)
    process.wait()

if __name__ == '__main__':
    main()