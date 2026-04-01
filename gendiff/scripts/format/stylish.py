# форматирование вывода в виде дерева
def format_value(value, depth, replacer=' ', spaces_count=2):
    indent = replacer * (depth * spaces_count)
    bracket_indent = replacer * ((depth - 1) * spaces_count)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(
                f"{indent}{k}: {format_value(
                    v,
                    depth + 1,
                    replacer,
                    spaces_count)}"
                )
        return "{\n" + "\n".join(lines) + "\n" + bracket_indent + "}"
    if value is None:
        return 'null'   
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


# форматирование вывода в виде дерева
def format_stylish(diff, replacer=' ', spaces_count=4, depth=1):
    indent = replacer * (spaces_count * depth)
    sign_indent = replacer * (spaces_count * depth - 2)
    lines = []
    for key, value in diff.items():
        status = value['status']
        if status == 'nested':
            children = format_stylish(
                value['children'],
                replacer,
                spaces_count,
                depth + 1
                )
            lines.append(f"{indent}{key}: {children}")

        elif status == 'added':
            val = format_value(
                value['value'],
                depth + 1,
                replacer,
                spaces_count)
            lines.append(f"{sign_indent}+ {key}: {val}")
        
        elif status == 'removed':
            val = format_value(
                value['value'],
                depth + 1,
                replacer,
                spaces_count)
            lines.append(f"{sign_indent}- {key}: {val}")

        elif status == 'unchanged':
            val = format_value(
                value['value'],
                depth + 1,
                replacer,
                spaces_count)
            lines.append(f"{indent}{key}: {val}")

        elif status == 'changed':
            old_val = format_value(
                value['old_value'],
                depth + 1,
                replacer,
                spaces_count)
            new_val = format_value(
                value['new_value'],
                depth + 1,
                replacer,
                spaces_count)

            lines.append(f"{sign_indent}- {key}: {old_val}")
            lines.append(f"{sign_indent}+ {key}: {new_val}")

    result = '\n'.join(lines)
    bracket_indent = replacer * ((depth - 1) * spaces_count)
    return "{\n" + result + "\n" + bracket_indent + "}"
