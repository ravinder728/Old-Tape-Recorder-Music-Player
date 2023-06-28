import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Old Tape Recorder Music Player")
        self.master.geometry("400x450")

        # Load the tape recorder image
        tape_recorder_image = Image.open("D:/Picture1.jpg")
        self.tape_recorder_photo = ImageTk.PhotoImage(tape_recorder_image)
        self.tape_recorder_label = tk.Label(master, image=self.tape_recorder_photo)
        self.tape_recorder_label.place(x=0, y=0)

        # Create the song listbox
        self.song_listbox = tk.Listbox(master, width=40, height=10)
        self.song_listbox.place(x=25, y=105)

        # Populate the song listbox with songs from a directory
        songs_directory = "D:/music"
        self.populate_song_listbox(songs_directory)

        # Create the buttons
        button_font = ('Arial', 13)
        self.play_button = tk.Button(master, text="▶", bg='black',fg='white', command=self.play,width=3,font=button_font)
        self.play_button.place(x=68,y=380)

        self.pause_button = tk.Button(master, text="⏸️",bg='black',fg='white',command=self.pause,font=button_font)
        self.pause_button.place(x=108, y=380)
        self.resume_button = tk.Button(master, text="⏏️",bg='black',fg='white', command=self.resume,font=button_font)
        self.resume_button.place(x=148, y=380)
        self.stop_button = tk.Button(master, text="⏹️",bg='red',fg='white', command=self.stop,width=3,font=button_font)
        self.stop_button.place(x=28, y=380)
        self.forward_button = tk.Button(master, text="⏭️", bg='black', fg='white', command=self.forward, width=3, font=button_font)
        self.forward_button.place(x=228, y=380)
        self.backward_button = tk.Button(master, text="⏮️", bg='black', fg='white', command=self.backward, width=3, font=button_font)
        self.backward_button.place(x=188, y=380)
        

        pygame.init()
        self.paused = False

    def populate_song_listbox(self, directory):
        songs = os.listdir(directory)
        for song in songs:
            if song.endswith(".mp3"):
                self.song_listbox.insert(tk.END, song)

    def play(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            selected_song = self.song_listbox.get(tk.ACTIVE)
            if selected_song:
                song_path = os.path.join("D:/music", selected_song)
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()

    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.paused = True

    def resume(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False
    def forward(self):
        pygame.mixer.music.stop()
        selected_song = self.song_listbox.get(tk.ACTIVE)
        if selected_song:
            song_index = self.song_listbox.curselection()[0]
            next_song_index = (song_index + 1) % self.song_listbox.size()
            self.song_listbox.selection_clear(0, tk.END)
            self.song_listbox.selection_set(next_song_index)
            self.song_listbox.activate(next_song_index)
            self.song_listbox.see(next_song_index)
            self.play()

    def backward(self):
        pygame.mixer.music.stop()
        selected_song = self.song_listbox.get(tk.ACTIVE)
        if selected_song:
            song_index = self.song_listbox.curselection()[0]
            prev_song_index = (song_index - 1) % self.song_listbox.size()
            self.song_listbox.selection_clear(0, tk.END)
            self.song_listbox.selection_set(prev_song_index)
            self.song_listbox.activate(prev_song_index)
            self.song_listbox.see(prev_song_index)
            self.play()


if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()



