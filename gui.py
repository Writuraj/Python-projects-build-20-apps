import functions
import PySimpleGUI as sg
import time

sg.theme('DarkBlue')

clock=sg.Text('',key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("test.txt"),
                      key='todos', enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("exit")


window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button,complete_button],
                           [exit_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=10)#run the loop every ten miliseconds
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos("test.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos("test.txt", todos)
            window['todos'].update(todos)
        case "Complete":
            try:
                todo_to_complete=values['todos'][0]
                todos = functions.get_todos("test.txt")
                todos.remove(todo_to_complete)
                functions.write_todos("test.txt", todos)
                window['todos'].update(values=todos)

                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item", font=('Helvetica', 20))
        case "Edit":
            try :
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos("test.txt")
                index = todos.index(todo_to_edit)

                todos[index] = new_todo + "\n"
                functions.write_todos("test.txt", todos)
            except IndexError:
                sg.popup("Please select an item",font=('Helvetica', 20))

            window['todos'].update(values=todos)
        case 'exit':
            break

        case "todos":
            window['todo'].update(value=values['todos'][0].strip())

        case sg.WIN_CLOSED:
            break

window.close()

