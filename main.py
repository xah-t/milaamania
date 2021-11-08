import os
import eyed3
import tempfile


def create_audiofiles_list(path_to_folder_with_files):
    """Функция создания списка аудиофайлов"""

    files_list = []
    with os.scandir(path_to_folder_with_files) as files:
        for f in files:
            if os.path.isfile(f):
                file_name_with_path = f"{path_to_folder_with_files}/{f.name}"
                files_list.append(file_name_with_path)
    return files_list


def create_directory_artist_album(audiofile_path):
    """Функция получения метаданных из аудиофайла"""
    """Params:
    audiofile_path:argument"""
    folder_with_files = "C:/python/milaamania/music"
    audiofile = eyed3.load(audiofile_path)  # "music/Madelyne - Beautiful Child (Hiver Hammer remix).mp3"
    """Настроить проверку, при которой название альбома и исполнителя не будет противоречить правилам названия папок."""
    imposible_symbols = "\/:*?<>|"
    for i in imposible_symbols:
        if i in audiofile.tag.album or audiofile.tag.artist or audiofile.tag.title:
            print("Imposible symbol")
    if audiofile.tag is None:
        base = os.path.basename(audiofile_path)
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
            base = os.path.basename(audiofile_path)
            if not os.path.isdir(f"{folder_with_files}/Исполнитель не определен"):
                os.makedirs(f"{folder_with_files}/Исполнитель не определен")
            os.replace(audiofile_path,
                       f"{folder_with_files}/Исполнитель не определен/{base}")
    else:
        if not os.path.isdir(f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.album}"):
            os.makedirs(f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.album}")
        os.replace(audiofile_path,
                   f"{folder_with_files}/{audiofile.tag.artist}/{audiofile.tag.album}/{audiofile.tag.artist}" + " - " + f"{audiofile.tag.title}.mp3")
    """
    - если в тегах нет исполнителя - сохранить в папку исполнитель не найден, имя файла не менять;
    - если в тегах нет альбома - сохранить в паку с названием исполнителя"""
    # print(f"Исполнитель: {audiofile.tag.artist}")
    # print(f"Альбом: {audiofile.tag.album}")
    # print(f"Альбом: {audiofile.tag.album_artist}")
    # print(f"Наименование: {audiofile.tag.title}")
    #audiofile.tag.album = "OST Shchnazzy - Portland 2003"  # присвоить альбому значение str
    #audiofile.tag.save()
    #path_artist = os.mkdir(f"C:/python/tests/milaamania/music/{audiofile.tag.artist}")
    #path_album = "C:/python/milaamania/music"
    """Настроить проверку наличия директории:
     - если есть исполнитель - провалиться в неё;
     - если есть альбом - провалиться в него"""

    # make_album_folder =  os.makedirs(f"{path_album}/{audiofile.tag.artist}/{audiofile.tag.album}")  # if есть директория, то пропустить
    # print(path_album)
    #
    # print(os.listdir(path=path_album))

    """Создать директорию и перенести файл в неё
    os.makedirs(f"{path_album}/{audiofile.tag.artist}/{audiofile.tag.album}")
    os.replace(audiofile_path,
               f"{path_album}/{audiofile.tag.artist}/{audiofile.tag.album}/{audiofile.tag.artist}" + " - " + f"{audiofile.tag.title}.mp3")"""
    """"""


if __name__ == "__main__":
    #create_directory_artist_album("music/Madelyne - Beautiful Child (Hiver & Hammer remix).mp3")
    music_path = "C:/python/milaamania/music"
    for i in create_audiofiles_list(music_path):
        print(i)
        create_directory_artist_album(i)

