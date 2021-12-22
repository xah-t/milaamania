import os
import eyed3
import logging
import io
import creating_directory


def check_is_mpthree():
    """Функция проверки типа файла"""
    """- Не аудиофайлы пропустить;
    - Аудиофайлы не мп3 сложить в один каталог"""
    pass


def check_tag(audiofile):
    """Подумать Lame tag CRC check failed"""
    base = os.path.basename(audiofile.path)
    if audiofile.tag is None:
        audiofile.initTag()
    if audiofile.tag.artist is None:
        audiofile.tag.artist = "Исполнитель не определен"
    if audiofile.tag.title is None:
        audiofile.tag.title = base
    if audiofile.tag.album is None:
        audiofile.tag.album = "Альбом не определен"
        audiofile.tag.save()
        return True


def replace_imposible_symbols(filename):
    """Замена недопустимых символов в имени файла
    Params: filename
    """

    audiofile = eyed3.load(filename)
    check_tag(audiofile)
    imposible_symbols = "\/:*?<>|"
    for i in imposible_symbols:
        if i in str(audiofile.tag.artist + audiofile.tag.album + audiofile.tag.title):
            print("Imposible symbol", f"'{i}' in {filename}")
            if i in audiofile.tag.artist:
                print("Imposible symbol in artist", f"'{i}'")
                str_ = audiofile.tag.artist
                audiofile.tag.artist = str_.replace(i, '')
                audiofile.tag.save()
            elif i in audiofile.tag.album:
                print("Imposible symbol in album", f"'{i}'")
                str_ = audiofile.tag.album
                audiofile.tag.album = str_.replace(i, '')
                audiofile.tag.save()
            else:
                print("Imposible symbol in title", f"'{i}'")
                str_ = audiofile.tag.title
                audiofile.tag.title = str_.replace(i, '')
                audiofile.tag.save()


def create_audiofiles_list(path_to_folder_with_files):
    """Функция создания списка
    Param: path_to_folder_with_files
    """
    """В цикле проходим по всем файлам в папке и сохраняем их названия в список"""
    #path_to_save = str(path_to_folder_with_files)
    files_list = []
    with os.scandir(path_to_folder_with_files) as files:
        for f in files:
            if os.path.isfile(f):
                replace_imposible_symbols(f)
                file_name_with_path = f"{path_to_folder_with_files}/{f.name}"
                files_list.append(file_name_with_path)
    return files_list#, path_to_save


if __name__ == "__main__":
    music_path = "C:/python/milaamania/music/На разбор"
    create_audiofiles_list(music_path)
    for i in create_audiofiles_list(music_path):
        print(i)

