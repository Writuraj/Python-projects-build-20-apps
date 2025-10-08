import streamlit as st
import functions as f


todos=f.get_todos("test.txt")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos("test.txt",todos)


st.title("My To-do app")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
st.checkbox("Buy groceries")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos("test.txt",todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ",placeholder="Enter a To do...",
              on_change=add_todo,key='new_todo')
