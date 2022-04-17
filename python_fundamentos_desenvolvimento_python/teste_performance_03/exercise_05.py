"""Escreva um programa em Python que leia nomes de alunos e suas alturas em metros
até que um nome de aluno seja o código de saída "Sair".
O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média
(a média aritmética das alturas de todos os alunos lidos)."""

import sys
from collections import namedtuple

Student = namedtuple('Student', ['name', 'height'])
students = []

fields = [
    {'label': 'Informe o nome do estudante:', 'valor': 0},
    {'label': 'Informe a altura do estudante em centimetros:', 'valor': 0},
]

def student_average(students):
    sum = 0
    for student in students:
        sum += int(student.height)
    return int(sum // len(students))


def student_filter(students):
    avg = student_average(students)
    students_avg = []
    for student in students:
        if int(student.height) > avg:
            students_avg.append(student.name)
    return [avg, students_avg]

def main():
    running = True
    while running:
        student = []
        for index, campo in enumerate(fields):
            if not running: continue

            while True:
                campo['valor'] = input(f"{campo['label']} ") or ''

                if index == 0 and campo['valor'] == 'Sair':
                    running = False
                    break

                if not campo['valor']:
                    print("O valor informado é inválido.")
                elif index == 1 and not campo['valor'].isnumeric():
                    print("O valor informado é inválido.")
                else:
                    student.append(campo['valor'])
                    break
        if len(student) == 2:
            students.append(Student(name=student[0], height=student[1]))
    result = student_filter(students)
    print(f"Os estudantes abaixo estão acima da média de {result[0]}cm")
    print("\n".join(result[1]))

if __name__ == "__main__":
    sys.exit(main())