from urllib.request import urlopen, Request
import urllib.error
import time
import sys

url = "https://site.teamorbi.net/cortex/current-version.txt"


def updateCheck(Version):
    try:
        req = Request(
            url,
            headers={"User-Agent": "ProjectCortex-Updater/1.0"}
        )
        with urlopen(req, timeout=5) as response:
            file_content = response.read().decode("utf-8").strip()

        if file_content == Version:
            print("Project Cortex is up to date!")
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
