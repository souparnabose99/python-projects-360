import FreeSimpleGUI as fsg
import to_do_functions as tdf

label = fsg.Text("Type in a To-Do item")
input_box = fsg.InputText(tooltip="Enter an item", key="todo")
add_button = fsg.Button("Add")

todo_display_window = fsg.Window("To-Do Application",
                                 layout=[[label], [input_box, add_button]],
                                 font=("Helvetica", 15))

while True:
    event, values = todo_display_window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = tdf.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            tdf.write_todos(todos)



todo_display_window.close()
