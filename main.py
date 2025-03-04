import json
import pyfiglet

# Load tasks from tasks.json
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

# Load font setting from font.json, default to "slant" font
try:
    with open("font.json", "r") as font:
        text = json.load(font).get("font", "slant")  # Default to "slant" font if no font is set
except (FileNotFoundError, json.JSONDecodeError):
    text = "slant"  # Default font if no font is set

# Verify if the font exists in pyfiglet
available_fonts = pyfiglet.FigletFont.getFonts()
if text not in available_fonts:
    print(f"Warning: '{text}' font not found. Using default 'slant' font.")
    text = "slant"  # Default to slant font if the chosen font is invalid

# Display the ToDoLS logo using the selected font
print(pyfiglet.figlet_format("ToDoLS", font=text))
print("A Tui To-Do List!")

def loop():
    choice = input("Type a command, or ? for commands:")

    normalized_choice = choice.strip().lower()

    if normalized_choice in ["?", "h", "help"]:
        print("Welcome to ToDoLS, A Tui To-Do List!")
        print("Commands:")
        print("? / h / help - for this menu")
        print("+ / add - add a task to the list")
        print("- / rm / remove - remove a task from the list")
        print("ls / list - list your tasks")
        print("q / quit - quit")
        print("Customization: ")
        print("font - change font of the logo")
        print("lsfnt / listfont - list all available fonts for the logo")
        loop()

    elif normalized_choice in ["+", "add"]:
        add = input("Add a task: ")
        tasks.append(add)
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        loop()
        
    elif normalized_choice in ["-", "rm", "remove"]:
        if tasks == []:
            print("Nothing to remove")
            loop()
        else:
            rm = input("Remove a task: ")
            tasks.remove(rm.strip().lower())
            with open("tasks.json", "w") as file:
                json.dump(tasks, file)
            loop()

    elif normalized_choice in ["ls", "list"]:
        for task in tasks:
            print(task)
        loop()

    elif normalized_choice in ["q", "quit"]:
        quit()

    elif normalized_choice in ["font"]:
        fonts = input("Enter logo font: ")
        text = fonts
        # Save the chosen font in font.json
        with open("font.json", "w") as font:
            json.dump({"font": text}, font)
        loop()

    elif normalized_choice in ["lsfnt", "listfont"]:
        print("Available fonts:", available_fonts)
        loop()
        
    else:
        print("Not a valid command, type ? for commands!")
        loop()

loop()

