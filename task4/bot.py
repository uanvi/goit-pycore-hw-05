from errhandler import input_error


def parse_input(user_input):
    """Parse bot command and arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error(2)
def add_contact(args, contacts):
    """Bot add command implementation
    """
    name, phone = args
    if name in contacts:
        return "Contact already exists. Please use the change command to modify."
    contacts[name] = phone
    return "Contact added."

@input_error(2)
def change_contact(args, contacts):
    """Bot change command implementation
    """
    name, phone = args
    if name not in contacts:
        return f"There is no contact with the name '{name}'"
    contacts[name] = phone
    return "Contact changed."

@input_error(0)
def get_all_contacts(args, contacts):
    """Bot all command implementation
    """
    return contacts

@input_error(1)
def get_phone_by_user(args, contacts):
    """Bot phone command implementation"""
    name = args[0]
    if name not in contacts:
        return f"There is no contact with the name '{name}'"
    return contacts[name]

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(get_all_contacts(args, contacts))
        elif command == "phone":
            print(get_phone_by_user(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
