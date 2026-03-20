# построение словаря с разницей между файлами

def build(old, new):
    diff = {}
    keys = sorted(old.keys() | new.keys())
    for key in keys:
        if key not in old:
            diff[key] = {
                'status': 'added',
                'value': new[key]
            }
        elif key not in new:
            diff[key] = {
                'status': 'removed',
                'value': old[key]
            }
        else:
            old_value = old[key]
            new_value = new[key]
            if isinstance(old_value, dict) and isinstance(new_value, dict):
                diff[key] = {
                    'status': 'nested',
                    'children': build(old_value, new_value)
                }
            elif old_value == new_value:
                diff[key] = {
                    'status': 'unchanged',
                    'value': old_value,
                }
            else:
                diff[key] = {
                    'status': 'changed',
                    'old_value': old_value,
                    'new_value': new_value
                }
    return diff