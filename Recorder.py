import ffmpeg
import time

def url_load():
    url_list = []
    with open("Songs", 'r') as file:
        lines = file.readlines()
        for line in range(0, len(lines)):
            song = (lines[line], "lyrics")
            videos_search = VideosSearch(song, limit=1)
            results = videos_search.result()
            if results['result']:
                video_url = results['result'][0]["link"]
                url_list.append(video_url)
        mpv_call(url_list)


def record_audio(title, duration, command):
    temp_video_file = f'{title}.mp4'
    input_video = ffmpeg.input(':0', format='x11grab', framerate=30)
    input_audio = ffmpeg.input('default', format='pulse')
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'{command}'])
    print(temp_video_file)
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(temp_video_file, t=duration).run(capture_stdout=True,
                                                                                                  capture_stderr=True)
    try:
        os.kill(signal.SIGTERM)
    except:
        pass


def youtubedlp_call(active_url, command):
    ydl_opts = dict(quiet=True, format='bestaudio/best', noplaylist=True, skip_download=True,
                    force_generic_extractor=True)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(active_url, download=False)
        duration = info.get('duration', None)
        title = info.get('title', None)
        title = ("'" + title + "'")
        with open('Titles', 'a') as file:
            file.write(title + '\n')
        record_audio(title, duration, command)


def mpv_call(url_list):
    p = 0
    afk_time = len(url_list) * 3
    print(f"Check on your PC again in {afk_time} Minutes \n - MAKE SURE AUTOMATIC SUSPEND IS DISABLED !")
    time.sleep(3)
    for i in range(len(url_list)):
        active_url = (url_list[p])
        command = f'mpv {active_url}'
        youtubedlp_call(active_url, command)
        p += 1

    with open("Songs", "w") as file:
        file.write('')


def main1():
    url_list = []
    with open("Songs", 'r') as file:
        lines = file.readlines()
        for line in range(0, len(lines)):
            song = lines[line]
            videos_search = VideosSearch(song, limit=1)
            results = videos_search.result()
            if results['result']:
                video_url = results['result'][0]["link"]
                url_list.append(video_url)
        mpv_call(url_list)

