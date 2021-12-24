from tkinter import *
from tkinter import font
import threading


def downloadFunc():
    downloader(url.get())


def downloader(video_url):
    from pytube import YouTube

    yt = YouTube(video_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first()
    yt.download('./')


if __name__ == "__main__":
    mainappwin = Tk()
    url = StringVar()

    mainappwin.geometry("500x500+500+100")
    mainappwin.title("Video Downloader")

    url_label = Label(mainappwin, text="Enter url here", font="Arial 15 bold")
    url_entry = Entry(mainappwin, textvariable=url)
    button_download = Button(mainappwin, text="Download",
                             font="Arial 13", fg="red", padx=5, pady=5, command=downloadFunc)
    url_label.pack()
    url_entry.pack()
    button_download.pack(pady=10)
    mainappwin.mainloop()
