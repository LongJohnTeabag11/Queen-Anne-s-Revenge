# Queen-Anne-s-Revenge
> MP3 file farming software using automated linux terminal commands.

## How to Use:
1. **Enter any song followed by the name of the artist (on the same line) into the 'Songs' file** - make sure their lyric video isn't 18+ restricted on YT otherwise it will not work. I have entered some into the file for an outline on how it should be formatted.
2. **The program will give you an estimated amount of time to leave your PC idle for** (this value is not to be believed exactly: it's calculated by multiplying the average song duration time by how many titles exist on the Songs.txt file).
4. **After all the recordings are complete and the idle time is over, you will be required to enter 'y' to every python console output saying a file is going to be overwritten**. This is the program converting the .mp4 files to .mp4.
5. **Finally, you can get rid of any remaining .mp4 files left in the directory** - inside the 'MPTHREE' directory is all the .mp3 files

## External Dependancies:
- You will be required to install ytdlp, ffmpeg and youtubesearchpython
- All of this can be done using the following Linux terminal commands:

```YoutubeDLP
pip install ytdlp
```
```FFMPEG
sudo apt install ffmpeg
```
```YoutubeSearchPython
pip install youtubesearchpython
```
