import streamlit as st
import function26

todos=function26.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function26.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo")
st.write("this app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function26.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add  new todo....",key="new_todo")


st.button("Add",key="add",on_click=add_todo)
