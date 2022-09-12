import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os
import eyed3


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('600x300')
        self.resizable(0, 0)
        self.title('Download music')

        # UI options
        self.paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.link = tk.StringVar()
        self.title = tk.StringVar()
        self.artist = tk.StringVar()
        self.album = tk.StringVar()

        # link
        username_label = ttk.Label(self, text="YT link:")
        username_label.grid(column=0, row=0, sticky=tk.W, **self.paddings)

        username_entry = ttk.Entry(
            self, textvariable=self.link, **entry_font, width=60)
        username_entry.grid(column=1, row=0, sticky=tk.E, **self.paddings)

        # title
        username_label = ttk.Label(self, text="Title:")
        username_label.grid(column=0, row=1, sticky=tk.W, **self.paddings)

        username_entry = ttk.Entry(
            self, textvariable=self.title, **entry_font, width=60)
        username_entry.grid(column=1, row=1, sticky=tk.E, **self.paddings)

        # artist
        password_label = ttk.Label(self, text="Artist:")
        password_label.grid(column=0, row=2, sticky=tk.W, **self.paddings)

        username_entry = ttk.Entry(
            self, textvariable=self.artist, **entry_font, width=60)
        username_entry.grid(column=1, row=2, sticky=tk.E, **self.paddings)

        # album
        password_label = ttk.Label(self, text="Album:")
        password_label.grid(column=0, row=3, sticky=tk.W, **self.paddings)

        username_entry = ttk.Entry(
            self, textvariable=self.album, **entry_font, width=60)
        username_entry.grid(column=1, row=3, sticky=tk.E, **self.paddings)

        # login button
        login_button = ttk.Button(
            self, command=self.afterClick, text="Download")
        login_button.grid(column=1, row=4, sticky=tk.E, **self.paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

    def afterClick(self):

        link = self.link.get()
        yt = YouTube(link)
        target = yt.streams.filter(
            only_audio=True, file_extension='mp4').first()
        print("download starts")
        target.download()
        print("downloaded")

        base_dir = "C:\\python\\YTDL\\"
        oldname = yt.title.replace(".", "").replace(
            ":", "").replace("'", "").replace("*", "").replace(",", "").replace("/", "").replace("$", "").replace("?", "").replace("\"", "").replace("#", "") + ".mp4"
        newname = self.title.get().replace(".", "").replace(
            ":", "").replace("'", "").replace("*", "").replace(",", "").replace("/", "").replace("$", "").replace("?", "").replace("\"", "").replace("#", "") + ".mp3"
        mp4 = "\"" + base_dir + oldname + "\""
        mp3 = "\"" + base_dir + "music\\" + newname + "\""
        cmd = "ffmpeg -i {} -vn {}".format(mp4, mp3)

        if not os.path.isdir(base_dir + "music"):
            os.mkdir(base_dir + "music")

        os.system(cmd)
        os.remove(oldname)

        file = eyed3.load("music\\" + newname)
        file.tag.title = self.title.get().replace(".", "").replace(":", "")
        file.tag.artist = self.artist.get().replace(".", "").replace(":", "")
        file.tag.album = self.album.get().replace(".", "").replace(":", "")
        file.tag.save()

        clabel = ttk.Label(
            self, text="File: " + newname + " is downloaded and saved.")
        clabel.grid(column=1, row=5, sticky=tk.W, **self.paddings)
        clabel.after(2000, clabel.destroy())


if __name__ == "__main__":
    app = App()
    app.mainloop()
