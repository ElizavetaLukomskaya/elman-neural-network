from utils import *

def predict():
    # p, L, alpha, e, sequence = input_parametrs()



    # input_matrix = generate_matrix(sequence, p, L+1)

    with open('matrix_1.txt', 'r') as file:
        matrix_1 = file.readlines()

    sequence_type = matrix_1[0]
    matrix_1 = [[float(n) for n in x.split()] for x in matrix_1[1:]]

    with open('matrix_2.txt', 'r') as file:
        matrix_2 = file.readlines()
    matrix_2 = [[float(n) for n in x.split()] for x in matrix_2]

    with open('context.txt', 'r') as file:
        context_matrix_elman = file.readlines()
    context_matrix_elman = [[float(n) for n in x.split()] for x in context_matrix_elman][0]

    L = len(matrix_1[0])
    p = len(matrix_1)-L
    sequence = []

    match (int(sequence_type)):
        case 1:
            a = int(input('Enter limit of sequence: '))
            sequence = period_sequence(a)
        case 2:
            a = int(input('Enter number: '))
            n = int(input('Enter limit of degree: '))
            sequence = degree_sequence(a, n)
        case 3:
            a = int(input('Enter number: '))
            n = int(input('Enter limit of progression: '))
            sequence = arithmetic_progression(a, n)
        case 4:
            n = int(input('Enter limit of sequence: '))
            sequence = fib(n)

    input_matrix = generate_matrix(sequence, p, L+1)


    for i in range(len(input_matrix)-1):
        output = step_predict(i, input_matrix, context_matrix_elman, matrix_1, matrix_2)
        output /= 100
        print(output)
