import subprocess


def convert(titles_list):
    for i in range(0, len(titles_list)):
        title_unedited = titles_list[i]
        mp3_name = title_unedited + ".mp3"
        try:
            open_slash = "''\\'"
            close_slash = "\\''"
            title_unedited1 = open_slash + title_unedited + close_slash + ".mp4'"
            file_path_MP3 = f"MPTHREE/{mp3_name}"
            com = f"ffmpeg -i {title_unedited1} -vn -ar 44100 -ac 2 -b:a 192k {file_path_MP3}"
            subprocess.run(com, shell=True)
        except:
            pass
        try:
            title_unedited2 = '"' + f"{title_unedited}" + '.mp4"'
            file_path_MP3 = f"MPTHREE/{mp3_name}"
            com = f"ffmpeg -i {title_unedited2} -vn -ar 44100 -ac 2 -b:a 192k {file_path_MP3}"
            subprocess.run(com, shell=True)
        except:
            pass
    with open("Titles", "w") as file:
        file.write('')


def main2():
    titles_list = []
    with open("Titles", "r") as file:
        lines = file.readlines()
        for line in range(0, len(lines)):
            title = lines[line]
            title = title.replace("\n", "")
            titles_list.append(title)
    convert(titles_list)


    convert(titles_list)


