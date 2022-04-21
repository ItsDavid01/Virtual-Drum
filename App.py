import tkinter as tk
import playsound as ps

class Bateria:
    def __init__(self,modo):
        self.modo = modo

class App:
    def grabar():
        pass
    def importar():
        pass

class Grabacion:
    def __init__(self,duracion,nombre,formato):
        self.duracion = duracion
        self.nombre = nombre
        self.formato = formato
    def reproducir():
        pass

class Platillo:
    def __init__(self,sonido_abierto,sonido_cerrado, root, nombre):
        self.sonido_abierto = sonido_abierto
        self.sonido_cerrado = sonido_cerrado
        
    def golpe_abierto():
        pass
    def golpe_cerrado():
        pass
    
class Tambor:
    def __init__(self,sonido,nombre,root, x, y):
        self.sonido = sonido
        self.nombre = nombre
        self.boton = tk.Button(root, text=nombre, command=self.golpe, padx=x, pady=y, bg="#428a6e")
    def golpe(self):
        print("sonido de", self.nombre)
        ps.playsound(self.sonido, block=False)

class Redoblante(Platillo): #herencia?
    def __init__(self,sonido_abierto,sonido_cerrado):
        super().__init__(self,sonido_abierto,sonido_cerrado)

class Bombo(Tambor): #herencia?
    def __init__(self,sonido,nombre,root, x, y):
        super().__init__(self,sonido)


app = tk.Tk()
app.geometry("1000x1000")

Redo = Tambor("redoblante.mp3", "Redoblante", app, 50, 50)
Redo.boton.grid(row=0 , column=2)

tom1 = Tambor("tom1.mp3", "Tom 1", app, 50,50)
tom1.boton.grid(row=0, column=0)

Bombo = Tambor("Bombo.mp3", "Bombo", app, 50,50)
Bombo.boton.grid(row=1, column=0)

platillo = Tambor("Platillo.mp3", "Platillo", app, 50,50)
platillo.boton.grid(row=0 , column=1)

HihatB = Tambor("HihatB.mp3", "", app, 60,50)
HihatB.boton.grid(row=1, column=1)

HihatA = Tambor("HihatA.mp3", "Hi Hat", app, 25,25)
HihatA.boton.grid(row=1, column=1)

app.mainloop()
