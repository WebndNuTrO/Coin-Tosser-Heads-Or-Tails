import random
from pyscript import display

def run_my_script():
    # Print the game title to the dark web terminal
    display("Coin Tosser", target="terminal-output")
    
    # Run your game logic
    tosser = random.randint(0, 1)
    
    if tosser == 0:
        display("Heads 🪙", target="terminal-output")
    else:
        display("Tails 🪙", target="terminal-output")
