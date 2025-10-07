from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)
while True :
    user_command = input("type add or show or edit or complete or exit")
    user_command = user_command.strip()
    if user_command.startswith('add') :
        todo = user_command[4:]

        todos=get_todos("test.txt")

        todos.append(todo+'\n')

        write_todos("test.txt",todos)

    elif user_command.startswith('show'):

        todos=get_todos("test.txt")

        for index,item in enumerate(todos):
                item=item.capitalize()
                item = item.strip('\n')
                if item :
                    print(f"{index+1}-{item}")

    elif user_command.startswith('edit') :
        try:
            number = int(user_command[5:])
            number = number-1

            todos = get_todos("test.txt")


            new_todo = input("enter a new todo : ")
            todos[number] = new_todo + '\n'

            write_todos("test.txt",todos)

        except ValueError:
            print("invalid input")
            continue

    elif user_command.startswith('complete') :
        try:
            number = int(user_command[9:])
            todos = get_todos("test.txt")
            todos_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)

            write_todos("test.txt",todos)

            message= f"todo {todos_to_remove} is completed"
            print(message)
        except IndexError:
            print("invalid input")
            continue
    elif 'exit' in user_command :
        break
    else :
        print("invalid command")

print("goodbye")