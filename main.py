import time
# Greeting
name = input("What should the program call you? ")
time.sleep(2)
print(f"Welcome, {name}.")
time.sleep(2)
# command line logic
while True:
    action = input("What would you like to do? Type '!help' for the command list: ")
    # Help command.
    if action == "!help":
        print("Key:")
        print("!greet: Program greets you.")
        print("!emoticon: Asks for which emoticon user prefers, then prints it.")
    # emoticon command
    elif action == "!emoticon":
        emoti = input("what kind of emoticon would you like? Type !help for a list of emoticons: ")
        print("INDEV")
   # greet command
    elif action == "!greet":
        print(f"Hey there, {name}! You are so coolsies bro")
    # Secret Touhou command, all roads lead to touhou
    elif action == "!touhou":
        print("...")
        time.sleep(2)
        print("Alright fine bro")
        # Prints terminal art of Reimu plushie