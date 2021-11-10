import os
import eyed3
import logging
import io


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


def replacce_imposible_symbols(filename):
    # log_stream = io.StringIO()
    # logging.basicConfig(stream=log_stream, level=logging.INFO)
    audiofile = eyed3.load(filename)
    # llog = log_stream.getvalue()
    # if llog:
    #     log_stream.truncate(0)
    check_tag(audiofile)
    imposible_symbols = "\/:*?<>|"
    for i in imposible_symbols:
        if i in str(audiofile.tag.artist + audiofile.tag.album + audiofile.tag.title):
            print("Imposible symbol", f"'{i}'")
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
    """Функция создания списка аудиофайлов"""
    """В цикле проходим по всем файлам в папке и сохранить их названия в список"""
    files_list = []
    with os.scandir(path_to_folder_with_files) as files:
        for f in files:
            if os.path.isfile(f):
                replacce_imposible_symbols(f)
                file_name_with_path = f"{path_to_folder_with_files}/{f.name}"
                files_list.append(file_name_with_path)
    return files_list


if __name__ == "__main__":
    music_path = "C:/python/milaamania/music"
    #create_audiofiles_list(music_path)
    for i in create_audiofiles_list(music_path):
        print(i)
