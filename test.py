import EmojiStore

from emojis import emojis

print()

emoji_list = EmojiStore.get_by_category('smileys_and_people')

for i in emoji_list:
    print()