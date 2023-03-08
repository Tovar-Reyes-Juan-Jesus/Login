from tkinter import *
from tkinter import ttk

class sesion:
    def __init__(self,raiz):
        raiz.title("Inicio de sesion")

        self.Usuario = StringVar()
        self.Contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding="14 14")
        mainFrame.grid(column=0, row= 0)

        UsuarioEntry= ttk.Entry(mainFrame, width=30, textvariable=self.Usuario)
        UsuarioEntry.grid( column= 1 , row= 1, columnspan=2)
        ContraseñaEntry= ttk.Entry(mainFrame, width=30, textvariable=self.Contraseña)
        ContraseñaEntry.grid(column=1, row= 3, columnspan= 2)
        
        ttk.Label(mainFrame, text="Nombre: ").grid(column= 0, row= 1, sticky=W)
        ttk.Label(mainFrame, text="").grid(column= 0, row= 2, columnspan=2)
        ttk.Label(mainFrame, text="Contraseña: ").grid(column= 0, row= 3, sticky=W)
        ttk.Label(mainFrame, text="").grid(column= 2, row= 4, columnspan=2)

        ttk.Button(mainFrame, text="Ingresar",command=self.Ingresar).grid(column= 2, row = 5, sticky=(E))
        UsuarioEntry.focus()
    def Ingresar(self, *args):
        print("Usuario Ingresado")
        #Usuario1 = 
        #Contraseña1 = 

        print("Usuario :", self.Usuario.get())
        print("Contraseña : ", self.Contraseña.get())


