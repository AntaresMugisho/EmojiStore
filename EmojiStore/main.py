from bs4 import BeautifulSoup
import requests

url = "https://www.webfx.com/tools/emoji-cheat-sheet/"
# response = requests.get(url)


def scrap():
    with open("../emoji.html", "r") as html:
        soup = BeautifulSoup(html, "html.parser")
        list = soup.select("div.apple.emojicon")

        url = list[0].find("img").get("src")
        print(url)

if __name__ == "__main__":
    scrap()