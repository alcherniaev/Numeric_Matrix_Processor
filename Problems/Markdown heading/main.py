def heading(message, level=1):
    if level <= 1:
        h = "#" * 1
        return f'{h} {message}'
    elif level > 6:
        h = "#" * 6
        return f'{h} {message}'
    else:
        h = "#" * level
        return f'{h} {message}'
