# https://github.com/theunreallpj ©️
# v1.1 of the YouTube Downloader 
# v1.0 -> https://github.com/theunreallpj/public-projects/blob/main/YouTubeDownloader/v1.0_downloader.py
#
# powered by: 
# -> PyTube: https://github.com/pytube/pytube
# -> customtkinter: https://github.com/TomSchimansky/CustomTkinter

from doctest import master
from multiprocessing.util import info
import customtkinter
from customtkinter import*
from tkinter import filedialog
import pytube
from pytube import*
import os
from os import path
import glob

def browsePath():
    path = filedialog.askdirectory()
    current_path_label.configure(text=path)
    
def downloading():
    video_link = link_entry.get()
    actual_path = current_path_label.text
    
    if format_var.get() == 1:
        yt = YouTube(video_link)
        audio = yt.streams.filter(only_audio=True).first()
        audio_file = audio.download(output_path=actual_path)
        base, ext = os.path.splitext(audio_file)
        end_audio_file = base + '.mp3'
        os.rename(audio_file, end_audio_file)
        #status_label.configure(text="Download was successful")
        status_label.configure(text="Download was successful !")
            
    elif format_var.get() == 2:
        yt = YouTube(video_link).streams.get_highest_resolution().download(output_path=actual_path)
        status_label.configure(text="Download was successful !")
   
    else:
        status_label.configure("ERROR !")

gui = customtkinter.CTk()
title = gui.title("YouTube Downloader")
gui.geometry("800x600")
gui.resizable(False, False)

link_entry = customtkinter.CTkEntry(master=gui, height=50, width=600, placeholder_text="paste your link here...")
link_entry.place(x=100, y=50)

format_label = customtkinter.CTkLabel(master=gui, height=40, text="Format :")
format_label.place(x=50, y=150)

format_var = IntVar()
format_mp3_radioButton = customtkinter.CTkRadioButton(master=gui, text="MP3", variable=format_var, value=1)
format_mp3_radioButton.place(x=200, y=160)
format_mp4_radioButton = customtkinter.CTkRadioButton(master=gui, text="MP4", variable=format_var, value=2)
format_mp4_radioButton.place(x=200, y=200)

path_text_label = customtkinter.CTkLabel(master=gui, height=40, text="Select download destination:")
path_text_label.place(x=90, y=250)

browse_path_btn = customtkinter.CTkButton(master=gui, width=90, height=40, text="Browse", command=browsePath)
browse_path_btn.place(x=290, y=250)

current_path_label = customtkinter.CTkLabel(master=gui, height=40, text="")
current_path_label.place(x=450, y=250)

download_btn = customtkinter.CTkButton(master=gui, height=60, width=300, text="Download", command=downloading)
download_btn.place(x=250, y=400)

status_label = customtkinter.CTkLabel(master=gui, height=40, text="")
status_label.place(x=300, y=500)



gui.mainloop()