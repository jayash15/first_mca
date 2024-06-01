import streamlit as st
import function
todos= function.get_todos()
def hellotodo():
    todo = st.session_state['newtodo'] #session_state is used to get todovalue
    todos.append(todo +'\n')
    function.write_todos(todos)
    st.session_state['newtodo'] = ""
st.title("mytodo_app")
st.subheader("todo")
st.text_input(label="",placeholder="add a todo",on_change=hellotodo,key='newtodo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=F"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        print(checkbox)
        function.write_todos(todos)
        del st.session_state[F"{todo}_{index}"]
        st.experimental_rerun() #it will automatically refresh the page

#print(st.session_state)
