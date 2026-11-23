#Package Imports
import time
from ascii_magic import AsciiArt

# Greeting
name = input("Hey! I'm commandline buddy! What should I call you? ")
time.sleep(2)
print(f"Hey there, {name}!")
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
    # Prints ASCII terminal art of Reimu plushie
    elif action == "!touhou":
        time.sleep(0.5)
        print("...")
        time.sleep(2)
        print("Alright fine bro")
        time.sleep(1)
        reimu = AsciiArt.from_image("reimu.png")
        reimu.to_terminal(columns=80)
    else: 
        print("Yeah I didn't understand that.")