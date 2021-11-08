import os
#import pathlib
import eyed3
import tempfile
from os import path
import re  #match


# def remove(value, deletechars):
#     for c in deletechars:
#         value = value.replace(c,'')
#     return value
# print remove(filename, '\/:*?"<>|')



audiofile = eyed3.load("C:/python/milaamania/music/Chillstep Deep Night.mp3")
pattern_ = '\/:*?"<>|'
str_ = str(audiofile.tag.artist + audiofile.tag.album + audiofile.tag.title)

print(str)
for i in pattern_:

    if i in str(audiofile.tag.artist + audiofile.tag.album + audiofile.tag.title):
        print ("Found", f"'{i}'")
# print(audiofile.tag.album)
# #pattern.search(audiofile.tag.album)
# # match = re.search(pattern, audiofile.tag.album)
# if re.search(pattern, audiofile.tag.album):
#     print("Found", pattern)
#
# def is_ok(text):
#
#     match = re.match("""^[а-яА-ЯёЁ][a-zA-Zа-яАё0-9 !?:;"'.,]+$""", text)
#     return bool(match)
#
#
# if __name__ == '__main__':
#     audiofile = eyed3.load("C:/python/milaamania/music/Cartoon - Howling [ @SpellMusic ].mp3")
#     for text in audiofile.tag.album:
#         print(is_ok(audiofile.tag.album), text)
