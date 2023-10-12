from bs4 import BeautifulSoup
import requests
import binascii

url = "https://www.webfx.com/tools/emoji-cheat-sheet/"
# response = requests.get(url)

categories = ["smileys_and_people", "animals_and_nature", "food_and_drink",  "travel_and_places", "activities",
              "objects", "symbols", "flags"]

def scrap():
    with open("../emoji.html", "r") as html:
        soup = BeautifulSoup(html, "html.parser")

        category = soup.select_one(f"div#{categories[0]}")
        item = category.select_one("div._item")
        description = item.get("data-alt-name")

        apple_emoji = item.select_one("div.apple.emojicon")
        image = apple_emoji.select_one("img")
        emoji = image.get("alt")
        emojicon_url = image.get("src")

        shortcode = item.select_one("div.shortcode").text
        unicode = item.select_one("div.unicode").text


        print(f"Category: {category.get('id')} \nDescription: {description} \nEmoji: {emoji} \nShortcode: {shortcode} \nUnicode: {unicode}")



if __name__ == "__main__":
    scrap()