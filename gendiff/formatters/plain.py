# форматирование вывода в виде плоского текста
def make_plain_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


# форматирование вывода в виде плоского текста
def format_plain(diff, path=''):
    lines = []

    for k, v in diff.items():
        status = v['status']
        curent_path = f"{path}{k}"
        if status == 'nested':
            children = format_plain(v['children'], f"{curent_path}.")
            lines.append(children)

        elif status == 'added':
            value = make_plain_value(v['value'])
            lines.append(
                f"Property '{curent_path}' was added with value: {value}"
                )
        elif status == 'removed':
            lines.append(f"Property '{curent_path}' was removed")
        
        elif status == 'changed':
            old_value = make_plain_value(v['old_value'])
            new_value = make_plain_value(v['new_value'])
            lines.append(
                f"Property '{curent_path}' was updated. "
                f"From {old_value} to {new_value}"
                )
    return '\n'.join(lines)