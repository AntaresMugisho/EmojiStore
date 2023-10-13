import os
import requests
import binascii
from bs4 import BeautifulSoup


def emojiconify(emoji_alias: str, data_uri: str):
    """
    Save emoji icon file from data_uri

    :param emoji_alias : Emoji alias
    :param data_uri : Data URI scheme containing the emoji image
    """

    extension = data_uri.partition("data:image/")[2].split(";")[0]
    path = os.path.join("emojicons", f"{emoji_alias}.{extension}")

    ascii_data = data_uri.partition("base64,")[2]

    with open(path, "wb") as file:
        file.write(binascii.a2b_base64(ascii_data))


def scrap(html):
    categories = ["smileys_and_people"] #, "animals_and_nature", "food_and_drink", "travel_and_places", "activities",
                  # "objects", "symbols", "flags"]

    soup = BeautifulSoup(html, "html.parser")
    count = 0

    for i, category in enumerate(categories):
        print(f"{i+1} => {category.upper()}")
        container = soup.select_one(f"div#{category}")
        items = [container.select_one("div._item")]

        for j, item in enumerate(items):
            description = item.get("data-alt-name")

            apple_emoji = item.select_one("div.apple.emojicon")
            image = apple_emoji.select_one("img")

            try:
                emoji = image.get("alt")
            except AttributeError:
                google_emoji = item.select_one("div.google.emojicon")
                image = google_emoji.select_one("img")

            emoji = image.get("alt")
            emojicon_data_uri = image.get("src")
            alias = item.select_one("div.shortcode").text[1:-1]
            unicode = item.select_one("div.unicode").text

            emojiconify(alias, emojicon_data_uri)

            count+= 1

            print(f"\t{i+1}.{j+1}=> Category: {category} Description: {description} Emoji: {emoji} Shortcode: {alias} Unicode: {unicode}")
        print(f"# ENDS WITH {j+1} EMOJIS #-----------------------------\n")

    print(f"# TOTAL OF {count} EMOJIS FOUND #-----------------------------")



if __name__ == "__main__":
    with open("../emoji.html", "r") as html:
        scrap(html)

    # url = "https://www.webfx.com/tools/emoji-cheat-sheet/"
    # response = requests.get(url)
    # html = response.text
    #
    # scrap(html)
