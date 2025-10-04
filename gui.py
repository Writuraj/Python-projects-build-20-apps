import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("test.txt"),key='todos',
                      enable_events=True, size = (45,10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]], font=('Helvetica', 12))

while True:
    event,values=window.Read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos("test.txt",todos)
            window['todos'].update(todos)
        case "Edit" :
            todo_to_edit=values['todos'][0]
            new_todo=values['todo']

            todos=functions.get_todos("test.txt")
            index=todos.index(todo_to_edit)
            todos[index]=new_todo
            functions.write_todos("test.txt",todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todos'].update(values['todos'][0])

        case sg.WINDOW_CLOSED():
            break

window.close()

