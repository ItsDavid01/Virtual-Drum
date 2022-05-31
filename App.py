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
import soundcard as sc
import soundfile as sf

import record as rd




        
        


class Tambor:
    def __init__(self, sonido, nombre, root, x, y):
        self.sonido = sonido
        self.nombre = nombre
        self.boton = tk.Button(root, text=nombre, command=self.golpe, padx=x, pady=y, bg="#428a6e")

    def golpe(self):
        print("sonido de", self.nombre)
        ps.playsound(self.sonido, block=False)



app = tk.Tk()
app.geometry("650x300")

grabar = rd.Grabacion(app,25, 25)
grabar.boton.grid(row=1, column=2)
grabar.playb.grid(row=1, column=3)
grabar.exportb.grid(row=1, column=4)

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
