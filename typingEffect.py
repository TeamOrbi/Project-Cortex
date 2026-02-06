import time
import sys

def type_message(message, delay=0.05):
    """
    Prints a message one character at a time with a delay between each character.
    
    Args:
        message (str): The message to type out
        delay (float): Delay in seconds between each character (default 0.05)
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Add a newline at the end



## AI WAS USED HERE
