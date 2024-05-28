import FreeSimpleGUI as fsg

label = fsg.Text("Type in a To-Do item")
input_box = fsg.InputText(tooltip="Enter an item")
add_button = fsg.Button("Add")

todo_display_window = fsg.Window("To-Do Application", layout=[[label], [input_box, add_button]])

todo_display_window.read()
todo_display_window.close()
