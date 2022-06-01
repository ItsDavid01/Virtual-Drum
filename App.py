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
        print("sonido de", self.nombre)
        ps.playsound(self.sonido, block=False)

        

        




app = tk.Tk()
app.title("Virtual Drum")
app.geometry("650x400")

grabar = rd.Grabacion(app, 100, 100)
grabar.boton.grid(row=1, column=2)
grabar.playb.grid(row=1, column=3)
grabar.exportb.grid(row=0, column=3)
grabar.recordLabel.grid(row=2, column=0)


Redo = Tambor("redoblante.mp3", "Redoblante", app, 150, 150, "Redoblante.png")
Redo.boton.grid(row=1, column=0)

tom1 = Tambor("tom1.mp3", "Tom 1", app, 150, 150, "tom1.png")
tom1.boton.grid(row=0, column=1)

Bombo = Tambor("Bombo.mp3", "Bombo", app, 150, 150, "Bombo.png")
Bombo.boton.grid(row=1, column=1)

platillo = Tambor("Platillo.mp3", "Platillo", app, 150, 150, "Platillo.png")
platillo.boton.grid(row=0, column=2)

HihatB = Tambor("HihatB.mp3", "", app, 150, 150, "Hihat.png")
HihatB.boton.grid(row=0, column=0)

HihatA = Tambor("HihatA.mp3", "Hi Hat", app, 70, 70, "Hihat.png")
HihatA.boton.grid(row=0, column=0)


app.mainloop()
