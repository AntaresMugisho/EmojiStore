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

        count = 0
        for i, category in enumerate(categories):
            print(f"{i+1} => {category.upper()}")
            container = soup.select_one(f"div#{category}")
            items = container.select("div._item")

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
                    emojicon_url = image.get("src")

                shortcode = item.select_one("div.shortcode").text
                unicode = item.select_one("div.unicode").text
                count+= 1

                print(f"\t{i+1}.{j+1}=> Category: {category} Description: {description} Emoji: {emoji} Shortcode: {shortcode} Unicode: {unicode}")
            print(f"# ENDS WITH {j+1} EMOJIS #-----------------------------\n")

        print(f"# TOTAL OF {count} EMOJIS FOUND #-----------------------------")


if __name__ == "__main__":
    scrap()