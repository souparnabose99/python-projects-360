import time
import FreeSimpleGUI as fsg
import to_do_functions as tdf

fsg.theme_previewer()
fsg.theme("DarkBrown")

clock = fsg.Text('', key='clock')
label = fsg.Text("Type in a To-Do item")
input_box = fsg.InputText(tooltip="Enter an item", key="todo")
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=tdf.get_todos(),
                       key="items",
                       enable_events=True,
                       size=(50, 7))
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Delete")
exit_button = fsg.Button("Exit")

todo_display_window = fsg.Window("To-Do Application",
                                 layout=[[clock],
                                         [label],
                                         [input_box, add_button],
                                         [list_box, edit_button, complete_button],
                                         [exit_button]],
                                 font=("Helvetica", 15))

while True:
    event, values = todo_display_window.read(timeout=200)
    todo_display_window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:

        case "Add":
            todos = tdf.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            tdf.write_todos(todos)
            todo_display_window["items"].update(values=todos)

        case fsg.WINDOW_CLOSED:
            break

        case "items":
            todo_display_window["todo"].update(value=values["items"][0])

        case "Delete":
            try:
                todo_to_complete = values["items"][0]
                todos = tdf.get_todos()
                todos.remove(todo_to_complete)
                tdf.write_todos(todos)
                todo_display_window["items"].update(values=todos)
                todo_display_window["todo"].update(value="")
            except IndexError:
                fsg.popup("Please select an item first.", font=("Helvetica", 20))

        case "Edit":
            try:
                todo_to_edit = values["items"][0]
                new_todo = values["todo"]

                todos = tdf.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                tdf.write_todos(todos)
                todo_display_window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item first.", font=("Helvetica", 20))

todo_display_window.close()
