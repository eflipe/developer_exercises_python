'''
Crear una matriz de 5x5 randomizada con números enteros,
encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar
la posición inicial y
final.
'''
import random
import pprint


def create_matrix():
    '''
    Crea una matriz de 5x5 randomizada con números enteros.

    :return: list

    >>> matriz_ejemplo = create_matrix()
    >>> len(matriz_ejemplo) == 5
    True
    >>> 0 <= matriz_ejemplo[0][0] <= 9
    True
    '''
    x = 5
    y = 5
    matriz = [[random.randint(0, 9) for x in range(x)] for i in range(y)]

    return matriz


def print_matrix(x, y, y_init, matrix, counter_rows=None, counter_cols=None):
    '''Printea la información sobre la posición inicial y final de los
       números encontrados consecutivamente'''
    if counter_rows:
        print("Cuatro números consecutivos encontrados en la fila número: ", x)
        print(f'La posicion inicial es: [{x}, {y_init}]')
        print(f'El número incial es: {matrix[x][y_init]}')
        print(f'La posicion final es: [{x}, {y}]')
        print(f'El número final es: {matrix[x][y]}')
    if counter_cols:
        print("Cuatro números consecutivos encontrados en la columna número: ", x)
        print(f'La posicion inicial es: [{y_init}, {x}]')
        print(f'El número incial es: {matrix[y_init][x]}')
        print(f'La posicion final es: [{y}, {x}]')
        print(f'El número final es: {matrix[y][x]}')


def iterate_matrix(matrix):
    '''
    Encuentra secuencia de 4 números consecutivos tanto
    horizontal como verticalmente.
    Printea la matriz.
    Si los encuentra, muestra la posición inicial y final de la secuencia de números.
    En caso contrario, imprime un mensaje de "No se encontraron secuencias de 4 números".

    :param list_dicts: list

    >>> matriz_ejemplo = [[9, 3, 4, 5, 6], [3, 2, 9, 0, 7], [4, 3, 8, 1, 8], [5, 3, 5, 2, 9], [6, 0, 1, 2, 3]]
    >>> iterate_matrix(matriz_ejemplo)
    Matriz:
    [[9, 3, 4, 5, 6],
     [3, 2, 9, 0, 7],
     [4, 3, 8, 1, 8],
     [5, 3, 5, 2, 9],
     [6, 0, 1, 2, 3]]
    Cuatro números consecutivos encontrados en la fila número:  0
    La posicion inicial es: [0, 1]
    El número incial es: 3
    La posicion final es: [0, 4]
    El número final es: 6
    Cuatro números consecutivos encontrados en la columna número:  0
    La posicion inicial es: [1, 0]
    El número incial es: 3
    La posicion final es: [4, 0]
    El número final es: 6
    Cuatro números consecutivos encontrados en la columna número:  4
    La posicion inicial es: [0, 4]
    El número incial es: 6
    La posicion final es: [3, 4]
    El número final es: 9
    Cuatro números consecutivos encontrados en la fila número:  4
    La posicion inicial es: [4, 1]
    El número incial es: 0
    La posicion final es: [4, 4]
    El número final es: 3
    >>> matriz_ejemplo_2 = [[4, 1, 9, 9, 0], [4, 2, 0, 0, 7], [8, 3, 9, 2, 8], [7, 8, 0, 7, 8], [2, 3, 4, 9, 0]]
    >>> iterate_matrix(matriz_ejemplo_2)
    Matriz:
    [[4, 1, 9, 9, 0],
     [4, 2, 0, 0, 7],
     [8, 3, 9, 2, 8],
     [7, 8, 0, 7, 8],
     [2, 3, 4, 9, 0]]
    No se encontraron secuencias de 4 números
    '''


    print("Matriz:")
    pprint.pprint(matrix)

    counter_rows = 0
    counter_cols = 0
    check_consecutive = False

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if y > 0:

                current_number_row = matrix[x][y]
                plus_prev_number_row = matrix[x][y - 1] + 1
                current_number_col = matrix[y][x]
                plus_prev_number_col = matrix[y - 1][x] + 1

                if current_number_row == plus_prev_number_row:  # checks rows
                    counter_rows += 1
                    if counter_rows == 3:
                        y_init = y - counter_rows
                        if y_init < 0:
                            break

                        print_matrix(x, y, y_init, matrix, counter_rows=counter_rows)

                        check_consecutive = True
                        counter_rows = 0
                else:
                    counter_rows = 0

                if current_number_col == plus_prev_number_col:  # checks cols
                    counter_cols += 1
                    if counter_cols == 3:
                        y_init = y - counter_cols

                        if y_init < 0:
                            break

                        print_matrix(x, y, y_init, matrix, counter_cols=counter_cols)
                        check_consecutive = True
                        counter_cols = 0

                else:
                    counter_cols = 0

    if not check_consecutive:
        print("No se encontraron secuencias de 4 números")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
