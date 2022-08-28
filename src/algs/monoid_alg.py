def monoid_table(symbols_list: list[tuple[str, list[int]]]) -> list[tuple[str, list[int]]]:
    if len(symbols_list) == 0:
        return None

    line_length = len(symbols_list[0][1])
    result_table: list[tuple[str, list[int]]] = [('e', [i + 1 for i in range(line_length)])]
    for item in symbols_list:
        result_table.append(item)
    equality_flag = False
    layer_counter = len(symbols_list)

    while layer_counter != 0:
        previous_counter = layer_counter
        layer_counter = 0
        for i in range(len(result_table) - previous_counter, len(result_table)):
            for item in symbols_list:
                current_line = (result_table[i][0] + item[0],
                                [item[1][j - 1] for j in result_table[i][1]])
                for m in range(len(result_table)):
                    if result_table[m][1] == current_line[1]:
                        equality_flag = True
                        break
                if not equality_flag:
                    result_table.append(current_line)
                    layer_counter += 1
                else:
                    equality_flag = False

    return result_table
