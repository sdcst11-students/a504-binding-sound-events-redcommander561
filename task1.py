
import tkinter as tk
from playsound import playsound
import threading


class FartBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Soundboard")

        
        button_configs = [
            ("perfect fart", "perfect-fart.mp3"),
            ("dry fart", "dry-fart.mp3"),
            ("reverb fart", "fart-with-reverb.mp3"),
            ("chill fart", "09037.mp3"),
            ("Loud fart", "fart9.mp3"),
            
        ]

        
        for text, sound_file in button_configs:
            tk.Button(self.root, text=text, command=lambda sf=sound_file: playsound(sf)).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = FartBoard(root)
    root.mainloop()

def play_sound(self,sound_file):
    threading.Thread(target=playsound,args=(sound_file,)).start()

#button configs= very cool and easier then making individual buttons 1 by 1

#john showed me what self.root does but I can not explain it


