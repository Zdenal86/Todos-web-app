import streamlit as sl
import modules.functions as fc


def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_to_file(todos)



todos = fc.read_from_file()


sl.title("My todo App")
sl.subheader("This is my todo App")
sl.text("You can check your todos")

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todos[index])
        fc.write_to_file(todos)
        del sl.session_state[todo]
        sl.rerun()
sl.text_input(label="Enter a todo", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")

# sl.session_state
