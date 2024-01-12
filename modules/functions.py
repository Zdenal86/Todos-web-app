import os
FILEPATH = "files/todos.txt"


def file_not_exist():
    if not os.path.exists("files/todos.txt"):
        try:
            with open("files/todos.txt", "w"):
                pass
        except FileNotFoundError:
            os.mkdir("files")
            with open("files/todos.txt", "w"):
                pass


def write_to_file(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_arg)


def read_from_file(filepath=FILEPATH):
    file_not_exist()
    with open(filepath, "r") as file_read:
        loc_todos = file_read.readlines()
    return loc_todos


def is_a_number(action, slice_number):
    if action[slice_number:].isdigit():
        return True
    else:
        return False





if __name__ == "__main__":
    print("Hello")
    print(read_from_file())
