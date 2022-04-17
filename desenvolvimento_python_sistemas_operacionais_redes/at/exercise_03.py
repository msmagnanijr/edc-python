"""Escreva um programa em Python que:
gere uma estrutura que armazena o nome dos arquivos em um determinado diretório e a quantidade de bytes que eles ocupam em disco.
Obtenha o nome do diretório do usuário.
Ordene decrescentemente esta estrutura pelo valor da quantidade de bytes ocupada em disco (pode usar as funções sort ou sorted);
gere um arquivo texto com os valores desta estrutura ordenados."""

import os
import sys

def get_list_of_files(directory):
    list_of_files = []
    for file in os.listdir(directory):
        list_of_files.append(directory + "/" + file)
    return list_of_files

def get_size_of_file_in_bytes(file):
    return os.path.getsize(file)


def create_report_header(report_file):
    try:
        with open(report_file, "w") as report:
            report.write("| File Name |  Size |\n")
            report.write("|-----------|-------|\n")
    except:
        print("Error creating report header")
    finally:
        report.close()

def create_report(list_of_files_and_size):
    try:
        with open("report.txt", "a+") as report:
            for file, size in list_of_files_and_size:
                file_name = file.split("/")[-1]
                report.write(f"{file_name} {size}\n")
    except:
        print("Error creating report")
    finally:
        report.close()

def print_report_file(report_file):
    try:
        with open(report_file, "r") as report:
            for line in report:
                print(line, end="")
    except:
        print("Error printing report file")
    finally:
        report.close()

def main():
    try:
        directory = input("Enter the directory: ")
        list_of_files = get_list_of_files(directory)
        list_of_files_and_size = []
        for file in list_of_files:
            list_of_files_and_size.append((file, get_size_of_file_in_bytes(file)))
        list_of_files_and_size.sort(key=lambda x: x[1], reverse=True)
        create_report_header("report.txt")
        create_report(list_of_files_and_size)
        print_report_file("report.txt")
    except FileNotFoundError:
        print("The directory does not exist")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    sys.exit(main())