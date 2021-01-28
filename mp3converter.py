import json as simplejson
import requests
from pytube import YouTube
from pydub import AudioSegment
AudioSegment.ffmpeg = "/path/to/ffmpeg"
from tkinter import *
import os

import glob
import lxml
import urllib
import urllib.request
from urllib.request import Request, urlopen
import pytube
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import time
import pathlib
from pathlib import Path
from os import path
import shutil



if __name__ =='__main__':
    root = Tk()
    root.title('YouTube Mp3 downloader')
    root.geometry("600x400")

    def myProcess():

        new_url = str(youtube_url.get())
        try:
            id = new_url.rsplit('/', 1)[1]

        except (IndexError, UnboundLocalError):
            messagebox.showinfo("error", "Invalid url, please try again.")
            print('invalid url')
            return False

        my_progress['value']=20
        root.update_idletasks()
        time.sleep(1)

        api_key = 'AIzaSyC7MRHUqlvGMYEDWZyRxR5mmkjsr1GusXk'
        url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}'
        header = {'USER-AGENT': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
        request = Request(new_url, headers=header)
        #print(youtube_url.get())

        my_progress['value']=50
        root.update_idletasks()
        time.sleep(1)

        yt = YouTube(youtube_url.get())
        title = yt.title


        youtube = pytube.YouTube(youtube_url.get()) #download video in mp4 format
        video = youtube.streams.first()
        video.download(pathlib.Path(__file__).parent.absolute())
        video_dir = pathlib.Path(__file__).parent.absolute()
        extension_list = ('*.mp4', '*.flv')

        my_progress['value']=80
        root.update_idletasks()
        time.sleep(1)

        os.chdir(video_dir) #extarct video mp3 and delete video mp4 format
        for extension in extension_list:
            for video in glob.glob(extension):
                mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
                AudioSegment.from_file(video).export(mp3_filename, format='mp3')
                os.remove(video)

        my_progress['value']=90
        root.update_idletasks()
        time.sleep(1)

        src = pathlib.Path(__file__).parent.absolute()
        dst = str(os.path.join(Path.home(), "Downloads"))

        files = [i for i in os.listdir(src) if i.endswith(".mp3") and path.isfile(path.join(src, i))] #move mp3 to users download folder
        for f in files:
            shutil.copy(path.join(src, f), dst)
            os.remove(f)


        my_progress['value']=100
        root.update_idletasks()
        time.sleep(1)

        myLabel_2 = Label(root, text= 'succesfully downloaded: '+ title) #message to indicate everything has been succesfull
        myLabel_2.pack()
        #print(title)
        return youtube


    myLabel = Label(root, text='enter video url:', font = ('Helvetica Neue', 12))
    myLabel.pack()

    youtube_url = Entry(root, width=20)
    youtube_url.pack()

    my_progress = ttk.Progressbar(root, orient=HORIZONTAL, mode='determinate')
    my_progress.pack(pady=20)

    myButton = Button(root, text="submit", command=myProcess)
    myButton.pack()



root.mainloop()
