def cayley_table(monoid_table: list[tuple[str, list[int]]]) -> list[list[str]]:
    if len(monoid_table) == 0:
        return None

    result_table: list[list[str]] = []
    table_length = len(monoid_table)

    for i in range(table_length):
        current_line = []
        for j in range(table_length):
            current_cell = [monoid_table[j][1][k - 1] for k in monoid_table[i][1]]
            for m in range(table_length):
                if monoid_table[m][1] == current_cell:
                    current_line.append(monoid_table[m][0])
                    break
        result_table.append(current_line)

    return result_table


def zero_element_check(cayley_table: list[list[str]]) -> tuple[list[str], list[str], list[str]]:
    left_zeros: list[str] = []
    right_zeros: list[str] = []

    for item in cayley_table:
        counter = 0
        current_element = item[0]
        for element in item:
            if element == current_element:
                counter += 1
        if counter == len(item):
            left_zeros.append(current_element)

    for i in range(len(cayley_table[0])):
        counter = 0
        current_element = cayley_table[0][i]
        for item in cayley_table:
            if item[i] == current_element:
                counter += 1
        if counter == len(cayley_table):
            right_zeros.append(current_element)

    zeros: list[str] = list(set(left_zeros) & set(right_zeros))

    return left_zeros, right_zeros, zeros


def inverse_element_check(cayley_table: list[list[str]]) -> tuple[list[str], list[str], list[str]]:
    left_invertible = []
    right_invertible = []

    for item in cayley_table:
        if not item[0] == 'e' and 'e' in item:
            left_invertible.append(item[0])

    for i in range(len(cayley_table[0])):
        current_element = cayley_table[0][i]
        for item in cayley_table:
            if not item[0] == 'e' and item[i] == 'e':
                right_invertible.append(current_element)
                break

    invertible = list(set(left_invertible) & set(right_invertible))

    return left_invertible, right_invertible, invertible


def group_check(cayley_table: list[list[str]]) -> tuple[bool, bool]:
    is_group = True
    is_commutative = False
    counter = 0
    cayley_table_length = len(cayley_table)

    if not len(cayley_table) - 1 == len(inverse_element_check(cayley_table)[2]):
        return False, False

    for i in range(cayley_table_length):
        for j in range(cayley_table_length):
            if cayley_table[i][j] == cayley_table[j][i]:
                counter += 1

    if counter == cayley_table_length * cayley_table_length:
        is_commutative = True

    return is_group, is_commutative
