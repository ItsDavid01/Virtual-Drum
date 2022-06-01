import tkinter as tk
import sounddevice as sd
import soundfile as sf
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
        
class Grabacion():
    def __init__(self, root, x, y) -> None:
        #Aqui se define la imagen que tendra cada boton, exportar, reproducir y grabar respectivamente
        #se abren las imagenes y se modifica el tipo de objeto para que concuerde con los paramtros dentro de la inicializacion del boton de tkinter
        self.exportButton = Image.open(r"Imagenes\ExportButton.jpeg")
        self.exportButton = self.exportButton.resize((x,y))
        self.exportButton = ImageTk.PhotoImage(self.exportButton)
        

        self.playButton = Image.open(r"Imagenes\PlayButton.jpg")
        self.playButton = self.playButton.resize((x,y))
        self.playButton = ImageTk.PhotoImage(self.playButton)

        self.recButton = Image.open(r"Imagenes\RecButton.jpg")
        self.recButton = self.recButton.resize((x,y))
        self.recButton = ImageTk.PhotoImage(self.recButton)


        #aqui definimos los atributos de la clase y los botones
        self.texto = "Grabar"
        self.boton = tk.Button(root, text=self.texto, command=self.Grabar, padx=x, pady=y, bg="#428a6e", image=self.recButton)
        self.playb = tk.Button(root, text="Play", command=self.play, padx=x, pady=y, bg="red", image=self.playButton)
        self.exportb = tk.Button(root, text="Export", command=self.export, padx=x, pady=y, bg="blue", image=self.exportButton)
        self.recordLabel = tk.Label(root, text = "No se está grabando", height = 10, width = 15)
        self.fs = 44100 #se define la frecuencia a la que se grabarán los audios
        self.root = root #root en este caso hará referencia a la ventana de tkinter que tenemos corriendo en el programa

    def Grabar(self):
        #para grabar primero le pediremos al usuario una duracion de grabación usando una simple caja de dialogo
        answer = simpledialog.askinteger("Duración", "Ingrese la duración de la grabación en segundos: ", parent=self.root, minvalue=0, maxvalue=100)
        if (answer != None):
            duration = answer  # la duracion especificada estará en segundos
            #se hace uso del método rec() perteneciente al modulo sounddevice para grabar en segundo plano los sonidos que se realicen con la bateria
            self.record = sd.rec(int(duration * self.fs), samplerate=self.fs, channels=2, device=" Mezcla estéreo (Realtek HD Audio Stereo input)")
            self.recordLabel.config(text = "Grabando") #cuando se empiece a grabar un texto en la parte inferior del programa nos mostrara que esta grabando
        else:
            messagebox.showwarning("Error","Valor de duración no válido, por favor ingrese otro.")

        

    def play(self):
        sd.stop()
        #una vez terminemos de grabar, lo que se grabó se guardara en un arreglo de NumPy y estara listo para reproducirse o exportarse
        sd.play(self.record, self.fs)
        self.recordLabel.config(text = "Grabación finalizada.")

    def export(self):
        #en caso de que se desee exportar, le pediremos el nombre bajo el cual desea exportar el archivo al usuario y procederemos a guardarlo en la carpeta del proyecto
        name = simpledialog.askstring("Nombre de la grabación", "Por favor, ingrese el nombre de la grabación: ", parent=self.root)
        if (name != None):
            #luego se convierte el arreglo de NumPy a un archivo de tipo WAV reproducible 
            file = sf.write(f"{name}.wav", self.record, self.fs)
            self.recordLabel.config(text = "Grabacion finalizada.")
        else:
            messagebox.showwarning("Error","Nombre de la grabación invalido, por favor intente de nuevo.")
        


        



        

