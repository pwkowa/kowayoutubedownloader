from pytube import YouTube as Y
import moviepy.editor as M
import os as o
import time as t
from colorama import init as I, Fore as F, Style as S

I()

def p():
    b = """
 _  __                        ____                      
| |/ /_____      ____ _      |  _ \  _____      ___ __  
| ' // _ \ \ /\ / / _` |_____| | | |/ _ \ \ /\ / / '_ \ 
| . \ (_) \ V  V / (_| |_____| |_| | (_) \ V  V /| | | |
|_|\_\___/ \_/\_/ \__,_|     |____/ \___/ \_/\_/ |_| |_|
    """
    c = [F.MAGENTA, F.RED]
    for i, l in enumerate(b.split('\n')):
        x = c[i % len(c)]
        print(x + l + S.RESET_ALL)
    t.sleep(2)

def d(u, f='mp4'):
    try:
        y = Y(u)
        v = y.streams.filter(only_audio=(f=='mp3')).first() if f == 'mp3' else y.streams.get_highest_resolution()
        d = v.download()

        if f == 'mp3':
            b, e = o.splitext(d)
            n = b + '.mp3'
            c = M.AudioFileClip(d)
            c.write_audiofile(n)
            c.close()
            o.remove(d)
            print(f"D and C to MP3: {n}")
        else:
            print(f"D video: {d}")

    except Exception as e:
        print(f"E: {e}")

def m():
    p()
    u = input("Enter the YouTube video URL: ")
    f = input("Enter the format (mp3 or mp4): ").lower()
    d(u, f)

if __name__ == "__main__":
    m()
