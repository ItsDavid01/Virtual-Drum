import playsound as ps
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
ps.playsound("HihatA.mp3")
import tkinter as tk
from pyparsing import col
import soundcard as sc
import soundfile as sf




class Grabacion():
    def __init__(self, root, x, y) -> None:
        self.texto = "grabar"
        self.boton = tk.Button(root, text=self.texto, command=self.Grabar, padx=x, pady=y, bg="#428a6e")
    def Grabar(self) -> None:
        print("GRabando")
        OUTPUT_FILE_NAME = "out.wav"    # file name.
        SAMPLE_RATE = 48000              # [Hz]. sampling rate.
        RECORD_SEC = 60                  # [sec]. duration recording audio.
        with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
            # record audio with loopback from default speaker.
            data = mic.record(numframes=SAMPLE_RATE*RECORD_SEC)
    
            # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
            print("Recorded")
            sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)
        self.texto = "grabando"
        


class Tambor:
    def __init__(self, sonido, nombre, root, x, y):
        self.sonido = sonido
        self.nombre = nombre
        self.boton = tk.Button(root, text=nombre, command=self.golpe, padx=x, pady=y, bg="#428a6e")

    def golpe(self):
        print("sonido de", self.nombre)
        ps.playsound(self.sonido, block=False)



app = tk.Tk()
app.geometry("450x300")

grabar = Grabacion(app,25, 25)
grabar.boton.grid(row=1, column=2)

Redo = Tambor("redoblante.mp3", "Redoblante", app, 50, 50)
Redo.boton.grid(row=0, column=2)

tom1 = Tambor("tom1.mp3", "Tom 1", app, 50, 50)
tom1.boton.grid(row=0, column=0)

Bombo = Tambor("Bombo.mp3", "Bombo", app, 50, 50)
Bombo.boton.grid(row=1, column=0)

platillo = Tambor("Platillo.mp3", "Platillo", app, 50, 50)
platillo.boton.grid(row=0, column=1)

HihatB = Tambor("HihatB.mp3", "", app, 60, 50)
HihatB.boton.grid(row=1, column=1)

HihatA = Tambor("HihatA.mp3", "Hi Hat", app, 25, 25)
HihatA.boton.grid(row=1, column=1)





app.mainloop()
