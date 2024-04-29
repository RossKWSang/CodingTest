def group_by_owners(file_dictionary):
    result = {}
    for key, value in file_dictionary.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result


print(group_by_owners({'Input.txt': 'Randy', 'Output.txt': 'Randy', 'Code.py': 'Stan'}))
