from urllib.request import urlopen, Request
import urllib.error
import time
import sys
import random

tombUrl = "https://site.teamorbi.net/tomb/current-version.txt"
cortexUrl = "https://site.teamorbi.net/cortex/current-version.txt"
orbilibUrl = "https://site.teamorbi.net/orbilib/current-version.txt"

orbiLib = '0.1.0'

def updateCheck(Version, project):
    if project == 'Tomb':
        url = tombUrl
    elif project == 'Cortex':
        url = cortexUrl
    elif project == 'OrbiLib':
        url = orbilibUrl
    try:
        req = Request(
            url,
            headers={"User-Agent": "TeamOrbi-InternetMaster/1.0"}
        )
        with urlopen(req, timeout=5) as response:
            file_content = response.read().decode("utf-8").strip()

        if file_content == Version:
            print("Project " + project + " is up to date!")
        else:
            print(
                f"Out of date. Your version: {Version}. "
                f"Latest version: {file_content}."
            )

    except urllib.error.URLError as e:
        print("Failed to retrieve the file:", e)


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
    print()

tombGreetings = ['Privacy is not for sale, and human rights should not be compromised out of fear or greed. - Pavel Durov', 'Why use a premade tool when I can make a crappy tool myself? - Orbernator']
cortexGreetings = ['The quiz game for that one person with some Buzz Controllers. And that browses GitHub. So just me. - Orbernator']

def greetingMessage(project):
    if project == 'Cortex':
        print(cortexGreetings[random.randint(0,0)])
    elif project == 'Tomb':
        print(tombGreetings[random.randint(0,1)])


def libUpdate():
    updateCheck(orbiLib, 'OrbiLib')
