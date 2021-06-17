'''
Hacer una función que genere una lista de diccionarios
que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la
lista sea de 10 elementos. Retornar la lista.
Hacer otra función que reciba lo generado en la primer
función y ordenarlo de mayor a menor.
Printear el id de la persona más joven y más vieja.
Devolver la lista ordenada.

'''
import random
from operator import itemgetter


def list_of_dicts():
    '''
    Genera una lista de diccionarios de 10 elementos.
    Las keys son "ID" y "Edad" donde edad es un número
    aleatorio entre 1 y 100.

    :return: list

    >>> test_list_of_dicts = list_of_dicts()
    >>> len(test_list_of_dicts) == 10
    True
    >>> 1 <= test_list_of_dicts[0]["Edad"] <= 100
    True
    '''
    LONG_LIST = 10
    list_dicts = []

    for element in range(1, LONG_LIST + 1):
        context_dict = {
            'ID': element,
            'Edad': random.randint(1, 101),
        }
        list_dicts.append(context_dict)

    return list_dicts


def sort_list(list_dicts):
    '''
    Recibe una lista y la ordena de mayor a menor.
    Printea el "ID" de la persona de mayor edad y la de menor edad.
    Devuelve la lista ordenada.

    :param list_dicts: list
    :return: list

    >>> ejemplo_lista =  [{'ID': 1, 'Edad': 51}, {'ID': 2, 'Edad': 54}, {'ID': 3, 'Edad': 31}, {'ID': 4, 'Edad': 74}, {'ID': 5, 'Edad': 21}, {'ID': 6, 'Edad': 19}, {'ID': 7, 'Edad': 77}, {'ID': 8, 'Edad': 62}, {'ID': 9, 'Edad': 85}, {'ID': 10, 'Edad': 29}]
    >>> sort_list(ejemplo_lista)
    ID y edad de persona mayor:
    ID: 9, Edad: 85
    ID y edad de persona menor:
    ID: 6, Edad: 19
    [{'ID': 9, 'Edad': 85}, {'ID': 7, 'Edad': 77}, {'ID': 4, 'Edad': 74}, {'ID': 8, 'Edad': 62}, {'ID': 2, 'Edad': 54}, {'ID': 1, 'Edad': 51}, {'ID': 3, 'Edad': 31}, {'ID': 10, 'Edad': 29}, {'ID': 5, 'Edad': 21}, {'ID': 6, 'Edad': 19}]
    '''

    sorted_list = sorted(list_dicts, key=itemgetter('Edad'), reverse=True)

    print(f'ID y edad de persona mayor:\nID: {sorted_list[0]["ID"]}, Edad: {sorted_list[0]["Edad"]}')
    print(f'ID y edad de persona menor:\nID: {sorted_list[-1]["ID"]}, Edad: {sorted_list[-1]["Edad"]}')

    return sorted_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
