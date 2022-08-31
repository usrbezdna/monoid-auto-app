from copy import deepcopy
from random import randint
from sys import path

from cayley_alg import cayley_table
from monoid_alg import monoid_table


path.insert(0, 'src/algs')


def generate(variants_number, nodes_number, symbols_number, queue, minimum=5, maximum=8):
    counter = 0
    current_list: list[tuple[str, list]] = [(symbol, [])
                                            for i, symbol in enumerate('abc') if i < symbols_number]
    start_tables: list[list[tuple[str, list]]] = []
    monoid_tables: list[list[tuple[str, list]]] = []
    cayley_tables = []

    while counter != variants_number:
        for _, line in current_list:
            line.clear()
            for _ in range(1, nodes_number + 1):
                line.append(randint(1, nodes_number))

        monoid_list = monoid_table(current_list)
        cayley_list = cayley_table(monoid_list)

        # minimum = 5 and maximum = 8 have optimal row and column values
        if minimum <= len(monoid_list) <= maximum:
            start_tables.append(deepcopy(current_list))
            monoid_tables.append(deepcopy(monoid_list))
            cayley_tables.append(deepcopy(cayley_list))
            counter += 1

    queue.put(start_tables)
    queue.put(monoid_tables)
    queue.put(cayley_tables)
