import tkinter as tk
import sounddevice as sd
import soundfile as sf
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
        
class Grabacion():
    def __init__(self, root, x, y) -> None:

        self.exportButton = Image.open(r"Imagenes\ExportButton.jpeg")
        self.exportButton = self.exportButton.resize((x,y))
        self.exportButton = ImageTk.PhotoImage(self.exportButton)
        

        self.playButton = Image.open(r"Imagenes\PlayButton.jpg")
        self.playButton = self.playButton.resize((x,y))
        self.playButton = ImageTk.PhotoImage(self.playButton)

        self.recButton = Image.open(r"Imagenes\RecButton.jpg")
        self.recButton = self.recButton.resize((x,y))
        self.recButton = ImageTk.PhotoImage(self.recButton)



        self.texto = "Grabar"
        self.boton = tk.Button(root, text=self.texto, command=self.Grabar, padx=x, pady=y, bg="#428a6e", image=self.recButton)
        self.playb = tk.Button(root, text="Play", command=self.play, padx=x, pady=y, bg="red", image=self.playButton)
        self.exportb = tk.Button(root, text="Export", command=self.export, padx=x, pady=y, bg="blue", image=self.exportButton)
        self.recordLabel = tk.Label(root, text = "No se está grabando", height = 10, width = 15)
        self.fs = 44100
        self.root = root

    def Grabar(self):
        answer = simpledialog.askinteger("Duración", "Ingrese la duración de la grabación en segundos: ", parent=self.root, minvalue=0, maxvalue=100)
        if (answer != None):
            duration = answer  # seconds
            self.record = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=2, device=" Mezcla estéreo (Realtek HD Audio Stereo input)")
            self.recordLabel.config(text = "Grabando")
        else:
            messagebox.showwarning("Error","Valor de duración no válido, por favor ingrese otro.")

        

    def play(self):
        sd.stop()
        sd.play(self.record, self.fs)
        self.recordLabel.config(text = "Grabación finalizada.")

    def export(self):
        name = simpledialog.askstring("Nombre de la grabación", "Por favor, ingrese el nombre de la grabación: ", parent=self.root)
        if (name != None):
            file = sf.write(f"{name}.wav", self.record, self.fs)
            self.recordLabel.config(text = "Grabacion finalizada.")
        else:
            messagebox.showwarning("Error","Nombre de la grabación invalido, por favor intente de nuevo.")
        


        



        

