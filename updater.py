from urllib.request import urlopen, Request
import urllib.error

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