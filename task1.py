
import tkinter as tk
from playsound import playsound

class FartBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Soundboard")

        
        button_configs = [
            ("perfect fart", "perfect-fart.mp3"),
            ("dry fart", "dry-fart.mp3"),
            ("reverb fart", "fart-with-reverb.mp3"),
            
        ]

        
        for text, sound_file in button_configs:
            tk.Button(self.root, text=text, command=lambda sf=sound_file: playsound(sf)).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = FartBoard(root)
    root.mainloop()





