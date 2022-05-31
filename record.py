import tkinter as tk
import sounddevice as sd
import soundfile as sf
from tkinter import simpledialog
from tkinter import messagebox
        
class Grabacion():
    def __init__(self, root, x, y) -> None:
        self.texto = "grabar"
        self.boton = tk.Button(root, text=self.texto, command=self.Grabar, padx=x, pady=y, bg="#428a6e")
        self.playb = tk.Button(root, text="play", command=self.play, padx=x, pady=y, bg="red")
        self.exportb = tk.Button(root, text="export", command=self.export, padx=x, pady=y, bg="blue")
        self.fs = 44100
        self.root = root

    def Grabar(self):
        answer = simpledialog.askinteger("duración", "Ingrese la duación de la grabación en segundos: ", parent=self.root, minvalue=0, maxvalue=100)
        if (answer != None):
            duration = answer  # seconds
            self.record = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=2, device=2)
        else:
            messagebox.showwarning("Error","valor de duración no válido, por favor ingrese otro")

        

    def play(self):
        sd.stop()
        sd.play(self.record, self.fs)

    def export(self):
        name = simpledialog.askstring("nombre de la grabación", "Por favor, ingrese el nombre de la grabación: ", parent=self.root)
        if (name != None):
            file = sf.write(f"{name}.wav", self.record, self.fs)
        else:
            messagebox.showwarning("Error","Nombre de la grabación invalido, por favor intente de nuevo")
        


        



        

