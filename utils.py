def query_handler(query, value, data, file_name):
    if query == 'filter':
        if data is None:
            file_data = read_file(file_name)
        else:
            file_data = data
        return filter(lambda v: value in v, file_data)
    elif query == 'map':
        if data is None:
            file_data = read_file(file_name)
        else:
            file_data = data
        return map(lambda v: v.split(' ')[int(value)], file_data)
    elif query == 'unique':
        if data is None:
            file_data = read_file(file_name)
        else:
            file_data = data
        return set(file_data)
    elif query == 'sort':
        if data is None:
            file_data = read_file(file_name)
        else:
            file_data = data
        if value == 'asc':
            return sorted(file_data, reverse=False)
        elif value == 'desc':
            return sorted(file_data, reverse=True)
    elif query == 'limit':
        if data is None:
            file_data = read_file(file_name)
        else:
            file_data = data
        return list(file_data)[:int(value)]


def read_file(file_name):
    with open(file_name) as f:
        for line in f:
            yield line
