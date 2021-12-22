import os
import eyed3
import tempfile
import re
from creating_lists import *


def create_path_to_save(audiofiles_path):
    """Функция формирования пути для сохранения файлов и папок после расфасовки
    Params: audiofiles_path"""
    # Разобраться с регуляркой, почему не находит выражение
    pattern = re.compile("[a-zA-Z]:\\((?:[a-zA-Z0-9() ]*\\)*)")
    folder_for_saving = re.match(pattern=pattern, string=audiofiles_path)
    folder_for_saving.group(0)
    #folder_for_saving = pattern.search(audiofiles_path)
    #re [a - zA - Z]:\\((?:[a-zA-Z0-9() ] *  \\) *).*
    #re [a-zA-Z]:\\((?:.*?\\)*).*
    print(folder_for_saving)



def create_directory_artist_album(audiofile_path):
    """Функция получения метаданных из аудиофайла
    Params:audiofile_path
    audiofile_path:argument"""
    folder_with_files = "C:/python/milaamania/music"
    base = os.path.basename(audiofile_path)
    audiofile = eyed3.load(audiofile_path)

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
    music_path = "C:/python/milaamania/music/На разбор"
    for i in create_audiofiles_list(music_path):
        create_path_to_save(i)
    # music_path = "C:/python/milaamania/music/На разбор"
    # for i in create_audiofiles_list(music_path):
    #     print(i)
    #     create_directory_artist_album(i)

