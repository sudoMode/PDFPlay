def is_pdf(path):
    return path.endswith('.pdf')


def flatten(nested_list):
    values = []
    for i in nested_list:
        if isinstance(i, list):
            for j in i:
                values.append(j)
        else:
            values.append(i)
    return values
