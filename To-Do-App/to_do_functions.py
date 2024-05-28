FILEPATH = r"Data\todo_items.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of to-do items
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todo_items, filepath=FILEPATH):
    """
    Write the to-do items in a text file
    """
    with open(filepath, "w") as file:
        file.writelines(todo_items)

