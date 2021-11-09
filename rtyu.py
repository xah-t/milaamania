import os
#import pathlib
import eyed3
import tempfile
from os import path
import re  #match
import logging
import io



# def remove(value, deletechars):
#     for c in deletechars:
#         value = value.replace(c,'')
#     return value
# print remove(filename, '\/:*?"<>|')

log_stream = io.StringIO()
logging.basicConfig(stream=log_stream, level=logging.INFO)
audiofile = eyed3.load('myfullfilename')
llog = log_stream.getvalue()
if llog:
    # deal here with the error message which in llog
    # and then purge the log_stream to reuse it for next eye3d call
    log_stream.truncate(0)
# all this code can be improved : enclose it in a try..catch, etc.

audiofile = eyed3.load("C:/python/milaamania/music/Foggy – Come Into My Dreams (Radio Edit).mp3")
pattern_ = '\/:*?"<>|'
str_ = str(audiofile.tag.artist + " - " +audiofile.tag.album + "; Album:" + audiofile.tag.title)

print(str_)
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
