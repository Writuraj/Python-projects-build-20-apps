import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("test.txt"),
                      key='todos', enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos("test.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos("test.txt", todos)
            window['todos'].update(todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos("test.txt")
                index = todos.index(todo_to_edit)

                todos[index] = new_todo + "\n"
                functions.write_todos("test.txt", todos)

                window['todos'].update(values=todos)
            except IndexError:
                pass

        case "todos":
            window['todo'].update(value=values['todos'][0].strip())

        case sg.WIN_CLOSED:
            break

window.close()

