import os
import eyed3
import tempfile
from creating_lists import *


def create_directory_artist_album(audiofile_path):
    """Функция получения метаданных из аудиофайла"""
    """Params:
    audiofile_path:argument"""
    folder_with_files = "C:/python/milaamania/music"
    base = os.path.basename(audiofile_path)
    audiofile = eyed3.load(audiofile_path)

    # """Настроить проверку, при которой название альбома и исполнителя не будет противоречить правилам названия папок."""
    # imposible_symbols = "\/:*?<>|"
    # for i in imposible_symbols:
    #     if i in str(audiofile.tag.artist + audiofile.tag.album + audiofile.tag.title):
    #         print("Imposible symbol", f"'{i}'")
    #         if i in audiofile.tag.artist:
    #             print("Imposible symbol in artist", f"'{i}'")
    #             str_ = audiofile.tag.artist
    #             audiofile.tag.artist = str_.replace(i, '')
    #             audiofile.tag.save()
    #         elif i in audiofile.tag.album:
    #             print("Imposible symbol in album", f"'{i}'")
    #             str_ = audiofile.tag.album
    #             audiofile.tag.album = str_.replace(i, '')
    #             audiofile.tag.save()
    #         else:
    #             print("Imposible symbol in title", f"'{i}'")
    #             str_ = audiofile.tag.title
    #             audiofile.tag.title = str_.replace(i, '')
    #             audiofile.tag.save()

    if audiofile.tag is None:
        if not os.path.isdir(f"{folder_with_files}/Исполнитель не определен"):
            os.makedirs(f"{folder_with_files}/Исполнитель не определен")
        os.replace(audiofile_path,
                   f"{folder_with_files}/Исполнитель не определен/{base}")
    elif audiofile.tag.album is None:
        if audiofile.tag.artist:
            if not os.path.isdir(f"{folder_with_files}/{audiofile.tag.artist}"):
                os.makedirs(f"{folder_with_files}/{audiofile.tag.artist}")
            os.replace(audiofile_path,
                       f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.artist}" + " - " + f"{audiofile.tag.title}.mp3")
        else:
            if not os.path.isdir(f"{folder_with_files}/Исполнитель не определен"):
                os.makedirs(f"{folder_with_files}/Исполнитель не определен")
            os.replace(audiofile_path,
                       f"{folder_with_files}/Исполнитель не определен/{base}")
    else:
        if not os.path.isdir(f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.album}"):
            os.makedirs(f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.album}")
        os.replace(audiofile_path,
                   f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.album}/{audiofile.tag.artist}" + " - " + f"{audiofile.tag.title}.mp3")


if __name__ == "__main__":
    #create_directory_artist_album("music/Madelyne - Beautiful Child (Hiver & Hammer remix).mp3")
    music_path = "C:/python/milaamania/music"
    for i in create_audiofiles_list(music_path):
        print(i)
        create_directory_artist_album(i)

