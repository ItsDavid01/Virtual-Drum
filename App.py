import playsound as ps
ps.playsound(r"Audios\HihatA.mp3")
ps.playsound(r"Audios\HihatA.mp3")
ps.playsound(r"Audios\HihatA.mp3")
ps.playsound(r"Audios\HihatA.mp3")
import tkinter as tk
from PIL import Image
from PIL import ImageTk

import record as rd

class Tambor:
    def __init__(self, sonido, nombre, root, x, y, image):
        self.sonido = sonido
        self.nombre = nombre
        self.image = Image.open(image)
        self.image = self.image.resize((x,y))
        self.image = ImageTk.PhotoImage(self.image)
        
        self.boton = tk.Button(root, text=nombre, command=self.golpe, padx=x, pady=y, bg="white", image=self.image, relief =tk.FLAT)

    def golpe(self):
        print("Sonido de", self.nombre)
        ps.playsound(self.sonido, block=False)

        
app = tk.Tk()
app.title("Virtual Drum")
app.geometry("650x400")

grabar = rd.Grabacion(app, 100, 100)
grabar.boton.grid(row=1, column=2)
grabar.playb.grid(row=1, column=3)
grabar.exportb.grid(row=0, column=3)
grabar.recordLabel.grid(row=2, column=0)


Redo = Tambor(r"Audios\redoblante.mp3", "Redoblante", app, 150, 150, r"Imagenes\Redoblante.png")
Redo.boton.grid(row=1, column=0)

tom1 = Tambor(r"Audios\tom1.mp3", "Tom 1", app, 150, 150, r"Imagenes\tom1.png")
tom1.boton.grid(row=0, column=1)

Bombo = Tambor(r"Audios\Bombo.mp3", "Bombo", app, 150, 150, r"Imagenes\Bombo.png")
Bombo.boton.grid(row=1, column=1)

platillo = Tambor(r"Audios\Platillo.mp3", "Platillo", app, 150, 150, r"Imagenes\Platillo.png")
platillo.boton.grid(row=0, column=2)

HihatB = Tambor(r"Audios\HihatB.mp3", "Hi Hat 2", app, 150, 150, r"Imagenes\Hihat.png")
HihatB.boton.grid(row=0, column=0)

HihatA = Tambor(r"Audios\HihatA.mp3", "Hi Hat", app, 70, 70, r"Imagenes\Hihat.png")
HihatA.boton.grid(row=0, column=0)


app.mainloop()
