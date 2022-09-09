# https://github.com/theunreallpj ©️
# v1.0 of a YouTube Downloader
# v1.0 inspired by The Code Dealer, on YT: https://www.youtube.com/c/MacLinzUniversalChannel
# tutorial link: https://www.youtube.com/watch?v=TEATfq6hPIg&list=WL&index=5&t=1470s
#
# powered by: 
# -> PyTube: https://github.com/pytube/pytube
# -> customtkinter: https://github.com/TomSchimansky/CustomTkinter
#changes made by @theunreallpj, on github: https://github.com/theunreallpj

from doctest import master
from multiprocessing.util import info
import customtkinter
from customtkinter import*
from tkinter import filedialog
import pytube
from pytube import*
import shutil


def changeCurrentPath():
    path = filedialog.askdirectory()
    current_path_label.configure(text=path)

def download():
    info_label.configure(text="downloading...")
    save_link = link.get()
    selected_path = current_path_label.text
    yt = YouTube(save_link).streams.get_highest_resolution().download()
    shutil.move(yt, selected_path)
    info_label.configure(text="Your video was downloaded !")

gui = customtkinter.CTk()
title = gui.title("YouTube Downloader")
gui.geometry("600x500")

link = customtkinter.CTkEntry(master=gui, width=500,  height=50, placeholder_text="paste your link here")
link.place(x=50, y=100)

path_label = customtkinter.CTkLabel(master=gui, text="Select download destination: ", height=40)
path_label.place(x=50, y=200)
path_btn = customtkinter.CTkButton(master=gui, height=40, width=60, text="Browse", command=changeCurrentPath)
path_btn.place(x=250, y=200)
current_path_label = customtkinter.CTkLabel(master=gui, height=40, text="")
current_path_label.place(x=350, y=200)

download_btn = customtkinter.CTkButton(master=gui, height=50, width=200, text="Download", command=download)
download_btn.place(x=200, y=300)

info_label = customtkinter.CTkLabel(master=gui, height=40, text="ready to download !")
info_label.place(x=200, y=400)

gui.mainloop()