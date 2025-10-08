import streamlit as st
import functions as f
todos=f.get_todos("test.txt")

st.title("My To-do app")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
st.checkbox("Buy groceries")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ",placeholder="Enter a To do...")