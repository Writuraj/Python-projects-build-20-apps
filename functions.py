def get_todos(file_path):
    """Read a text file and return the list of todos"""
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(file_path,todos_arg):
    """Write a list of todos to a text file"""
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)