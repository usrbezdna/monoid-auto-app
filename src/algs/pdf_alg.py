from copy import copy
from functools import reduce
from pylatex import Document, Section, Subsection, Tabular

from cayley_alg import cayley_table


def pdf4_tables(filepath_to_out: str, section_name: str,
                nodes_number: int, *data: list[list[tuple[str, list]]]):

    geometry_options = {
        "head": "0pt",
        "margin": "0.5in",
        "bottom": "0.5in",
        "includeheadfoot": False
    }

    doc = Document("multirow", indent=False, geometry_options=geometry_options)
    section = Section(section_name)

    vertices_count = nodes_number

    table_template = '|c' * vertices_count + '|c|'

    for single_table_data in data:
        new_subsect = Subsection('')
        table = Tabular(table_template)

        table.add_hline()
        vert_headers = [j for j in range(1, vertices_count + 1)]
        vert_headers.insert(0, "")

        table.add_row((vert_headers))
        table.add_hline()

        for single_line in single_table_data:
            row = [single_line[0]] + single_line[1]
            table.add_row(row)
            table.add_hline()

        new_subsect.append(table)
        section.append(new_subsect)

    doc.append(section)
    doc.generate_pdf(filepath=filepath_to_out, compiler='pdflatex')


def pdf4_cayley(filepath_to_out: str, *
                cayley_data: list[list[tuple[str, list]]]):
    geometry_options = {
        "head": "0pt",
        "margin": "0.5in",
        "bottom": "0.5in",
        "includeheadfoot": False
    }

    doc = Document("multirow", indent=False, geometry_options=geometry_options)
    section = Section('Cayley tables')

    for tables_data in cayley_data:

        vert_header = tables_data[0]
        hor_veader = copy(vert_header)

        hor_veader.insert(0, '')

        table_size = len(vert_header)
        table_template = '|c' * table_size + '|c|'

        new_subsect = Subsection('')
        table = Tabular(table_template)

        table.add_hline()
        table.add_row(hor_veader)
        table.add_hline()

        for i, line_data in enumerate(tables_data):
            row = [vert_header[i]] + line_data
            table.add_row(row)
            table.add_hline()

        new_subsect.append(table)
        section.append(new_subsect)

    doc.append(section)
    doc.generate_pdf(filepath=filepath_to_out, compiler='pdflatex')
