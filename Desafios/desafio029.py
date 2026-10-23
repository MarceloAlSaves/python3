print("Interactive helping system in Python")
def interactive_help():
    print("Welcome to the interactive help system!")
    print("Type 'exit' to quit.")
    
    while True:
        command = input("Enter a command or function name: ")
        if command.lower() == 'exit':
            print("Exiting the help system. Goodbye!")
            break
        else:
            try:
                help(eval(command))
            except Exception as e:
                print(f"Error: {e}. Please enter a valid command or function name.")


