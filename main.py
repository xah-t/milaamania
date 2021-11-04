import os, eyed3, tempfile


"""Функция создания списка аудиофайлов"""
def create_audiofiles_list(path_to_folder_with_files):
    """В цикле пройти по всем файлам в папке и сохранить их названия в список"""
    files_list = []
    for f in os.listdir(path_to_folder_with_files):
        file_name_with_path = f"{path_to_folder_with_files}/{f}"
        files_list.append(file_name_with_path)
    return (files_list)
    #print(files_list)


def create_directory_artist_album(audiofile_path):
    """Функция получения метаданных из аудиофайла"""
    """Params:
    audiofile_path:argument"""

    audiofile = eyed3.load(audiofile_path)  # "music/Madelyne - Beautiful Child (Hiver Hammer remix).mp3"
    """Настроить условие: 
    - если в тегах нет исполнителя - сохранить в папку исполнитель не найден, имя файла не менять;
    - если в тегах нет альбома - сохранить в паку с названием исполнителя"""
    print(f"Исполнитель: {audiofile.tag.artist}")
    print(f"Альбом: {audiofile.tag.album}")
    print(f"Альбом: {audiofile.tag.album_artist}")
    print(f"Наименование: {audiofile.tag.title}")
    #audiofile.tag.album = "OST Shchnazzy - Portland 2003"  # присвоить альбому значение str
    #audiofile.tag.save()
    #path_artist = os.mkdir(f"C:/python/tests/milaamania/music/{audiofile.tag.artist}")
    path_album = "C:/python/tests/milaamania/music"
    """Настроить проверку наличия директории:
     - если есть исполнитель - провалиться в неё;
     - если есть альбом - провалиться в него"""

    make_album_folder =  os.makedirs(f"{path_album}/{audiofile.tag.artist}/{audiofile.tag.album}")  # if есть директория, то пропустить
    print(path_album)

    print(os.listdir(path=path_album))

    """Перенести файл в созданную директорию"""
    os.replace(audiofile_path,
               f"{path_album}/{audiofile.tag.artist}/{audiofile.tag.album}/{audiofile.tag.artist}" + " - " + f"{audiofile.tag.title}.mp3")
    """"""


if __name__ == "__main__":
    #create_directory_artist_album("music/Madelyne - Beautiful Child (Hiver & Hammer remix).mp3")
    music_path = "C:/python/tests/milaamania/music"
    for i in create_audiofiles_list(music_path):
        print(i)
        create_directory_artist_album(i)

