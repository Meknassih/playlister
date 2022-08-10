from tkinter import *
from playlist import *
import threading

version = 1.0
winheight = 400
winwidth = 600
window = Tk()
spotdl_thread = None

# Use https://github.com/jackmcarthur/musical-key-finder to find keys


def main():

    window.title("Playlister " + str(version))
    window.resizable(0, 0)
    window.geometry(str(winwidth) + "x" + str(winheight))

    lbl = Label(window, text="Playlist URL")
    lbl.grid(column=0, row=0)

    txt = Entry(window, width=50)
    txt.insert(
        0, "https://open.spotify.com/playlist/5nNKoQXqMu3HoAoo6EScgv?si=9f06fb68358a4dbc")
    txt.grid(column=1, row=0)

    def handle_create():
        global spotdl_thread
        spotdl_thread = threading.Thread(
            None, createPlaylist, args=(txt.get(),), name="spotdl")
        spotdl_thread.start()
        for thread in threading.enumerate():
            print(str(thread.name))

    create_btn = Button(window, text="Create", command=handle_create)
    create_btn.grid(column=2, row=0)

    status_lbl = Label(window, text="Idle")
    status_lbl.grid(column=1, row=1)

    while True:
        try:
            window.update_idletasks()
            window.update()
            if spotdl_thread != None and spotdl_thread.is_alive():
                print(f"Spotdl thread alive")
                status_lbl.configure(text="Creating playlist...")
                create_btn["state"] = "disabled"
            else:
                status_lbl.configure(text="Idle")
                create_btn["state"] = "normal"
        except:
            return 0


main()
