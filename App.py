import playsound as ps
ps.playsound(r"Audios\HihatA.mp3")
ps.playsound(r"Audios\HihatA.mp3")
ps.playsound(r"Audios\HihatA.mp3")
ps.playsound(r"Audios\HihatA.mp3")
import tkinter as tk
from PIL import Image
from PIL import ImageTk

import record as rd

class Tambor: #clase tambor para definir los componentes de la bateria
    def __init__(self, sonido, nombre, root, x, y, image):
        self.sonido = sonido
        self.nombre = nombre
        #aqui se define la imagen que va a tener el componente de la bateria, este se convierte a un objeto imagen reconocible por tkinter primero
        self.image = Image.open(image)
        self.image = self.image.resize((x,y))
        self.image = ImageTk.PhotoImage(self.image)
        
        #Se define el boton que al presionarse va a llamar el método golpe()
        self.boton = tk.Button(root, text=nombre, command=self.golpe, padx=x, pady=y, bg="white", image=self.image, relief =tk.FLAT)

    def golpe(self):
        print("Sonido de", self.nombre)
        ps.playsound(self.sonido, block=False) #con la ayuda de playsound se reproduce el sonido correspondiente que esta guardado dentro de la carpeta sonidos

        
app = tk.Tk() #se inicializa la ventana principal de tkinter
app.title("Virtual Drum") #aqui se cambia el titulo de la ventana
app.geometry("650x400") # y aqui se establecen las dimensiones (AltoxAncho) que va a tener la ventana cuando se ejecute el programa

#a continuacion creamos una instancia de la clase grabacion para obtener los botones de grabar, reproducir, y exportar
#asi mismo tambien les asignamos una posición dentro de la ventana con el metodo .grid()
grabar = rd.Grabacion(app, 100, 100)
grabar.boton.grid(row=1, column=2)
grabar.playb.grid(row=1, column=3)
grabar.exportb.grid(row=0, column=3)
grabar.recordLabel.grid(row=2, column=0)

#tambien creamos instancias de la clase Tambor para obtener los diferentes componentes de la bateria
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


app.mainloop() #Esta linea de código marca el final de la ventana que el módulo tkinter nos ofrece
