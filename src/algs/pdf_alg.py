from pylatex import Document, Section, Subsection, Tabular

def pdf4_start_tables(*data: list[list[tuple[str, list]]]):
    
    geometry_options = {
        "head": "0pt",
        "margin": "0.5in",
        "bottom": "0.5in",
        "includeheadfoot": False
}
    doc = Document("multirow", indent=False, geometry_options=geometry_options)
    section = Section('Variants')

    vertices_count = len(data[0][0][1])

    table_template = '|c' * vertices_count + '|c|'

    for i, single_table_list in enumerate(data):
        new_subsect = Subsection('')
        table = Tabular(table_template)

        table.add_hline()
        vert_headers = [j for j in range(1, vertices_count+1)]
        vert_headers.insert(0, "")

        table.add_row((vert_headers))
        table.add_hline()

        for tuple_ in single_table_list:
            row = list(tuple_[0]) + tuple_[1]
            table.add_row(row)
            table.add_hline()
            

        new_subsect.append(table)
        section.append(new_subsect)
    
    doc.append(section)
    doc.generate_pdf(filepath='gen_files/start_tables', compiler='pdflatex')
