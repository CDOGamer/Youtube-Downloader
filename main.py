# imports
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

import pytube
import youtube_dl
import os
from moviepy.editor import *
import glob

def mp3():
    # Not working
    mp4_file = r'C:/Users/lucas/Documents/YT/Amon Amarth - Live in Oberhausen December. 14. 2019 (Full Concert Pro Shot).mp4'
    mp3_file = r'C:/Users/lucas/Documents/YT/Amon Amarth - Live in Oberhausen December. 14. 2019 (Full Concert Pro Shot).mp3'
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


# def fürs Downloaden
def download():
    if entryMain.get() == "":
        messagebox.showerror("Achtung!", "Bitte gebe ein Link ein.")
        return
    try:
        path = 'C:/Users/lucas/Documents/YT'
        video_url = entryMain.get()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        if choice.get() == "MP3":

            video.download(path)
            return
        if choice.get() == "MP4":
            video.download(path)

    except:
        messagebox.showerror("Achtung!", "Bitte gebe ein gültigen Link ein.")
        return


# mainWindows
main = Tk()
main.title('Downloader')
main.wm_geometry('200x200')
# generate Labels...s
choice = StringVar()

progress = Progressbar(master=main, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
progress.place(x=1, y=140, width=40, height=20)

labelMain = Label(master=main, text='Link des YouTube Videos.')
entryMain = Entry(master=main, text='Link...')
button = Button(master=main, text='Download', command=download)

radiobutton1 = Radiobutton(master=main, anchor='w',
                           text='MP3', value='MP3', variable=choice)
radiobutton1.place(x=1, y=60, width=150, height=20)
radiobutton2 = Radiobutton(master=main, anchor='w',
                           text='MP4', value='MP4', variable=choice)
radiobutton2.place(x=1, y=90, width=150, height=20)
radiobutton1.select()
# set Labels....
labelMain.place(x=1, y=1, width=150, height=30)
entryMain.place(x=1, y=30, width=150, height=30)
button.place(x=1, y=120, width=150, height=30)

main.mainloop()
