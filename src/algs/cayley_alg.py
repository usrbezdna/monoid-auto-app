def cayley_table(monoid_table: list[tuple[str, list[int]]]) -> list[list[str]] | None:
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
