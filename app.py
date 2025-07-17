from colorama import Fore, Style, init
import os
import json

# Colors
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
c = Fore.LIGHTCYAN_EX
re = Fore.RESET

# Styles
dim = Style.DIM
res = Style.RESET_ALL

# Create data.json file, if not existed
if not os.path.exists("data.json"):
    with open("data.json", "w", encoding='utf-8') as file:
        json.dump([], file, indent=4)


class ToDo:
    def __init__(self):
        # List of commands
        self.commands = [
            {
                "name": "add",
                "func": self.add,
                "text": "Adds a new to do item"
            },
            {
                "name": "list",
                "func": self.list_all,
                "text": "Shows all to do items"
            },
            {
                "name": "exit",
                "func": self.close,
                "text": "Closes this program"
            }
        ]

        # Print commands
        for command in self.commands:
            # Format: [*] add     Adds a new todo item
            print(f"{c}[*] {re}{'{:<7}'.format(command["name"])} {dim}{command["text"]}{res}")

        # run prompt function for user input
        self.prompt()

    
    def prompt(self):
        choose = input(f"{y}[+] {re}")

        not_found = True

        # Compare choose with name of command list
        for command in self.commands:
            if choose == command["name"]:
                not_found = False
                # Run function of found command
                command["func"]()

        # Check if not_found (True)
        if not_found:
            print("")
            # Print error message
            print(f"{r}[!] {re}Command {r}{choose}{re} not found.")
            print("")
            # Run the prompt function again
            self.prompt()


    def add(self):
        print("")

        # Input for date, time and to do
        date = input(f"{y}[+] Date (yyyy-mm-dd): {re}")
        t = input(f"{y}[+] Time (hh:mm): {re}")
        todo = input(f"{y}[+] To Do: {re}")

        print("")

        # Reading existing data
        with open("data.json", "r", encoding='utf-8') as file:
            data = json.load(file)

        # Adding values to data
        data.append(
            {
                "date": date,
                "time": t,
                "todo": todo
            }
        )

        # Write new data to file
        with open("data.json", "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        # Execute prompt
        self.prompt()


    def list_all(self):
        # Reading data
        with open("data.json", "r", encoding='utf-8') as file:
            data = json.load(file)

        print("")

        # Listing all items of data
        for index, item in enumerate(data, 1):
            print(f"{c}{'{:03d}'.format(index)} {re}{dim}{item['date']} {item['time']} {res}{c}| {re}{item['todo']}")

        print("")

        # Execute prompt
        self.prompt()


    def close(self):
        print(f"{r}[!] {re}Bye.")
        quit()


# Execute ToDo (init)
ToDo()