import os
import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from user.user_main import User
from settings import VISTAS

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.ico = Image.open(os.path.join(os.getcwd(), 'img', 'logo.png'))
        self.foto = ImageTk.PhotoImage(self.ico)
        self.wm_iconphoto(False, self.foto)

        self.title('Revision')
        self.geometry('500x500')
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure(0, weight=1)


# ------------------------      MENU      --------------------------------


        self.barra_menu = tk.Menu(self)
        self.info = tk.Menu(self.barra_menu, tearoff=False)
        self.barra_menu.add_command(label='Informacion')
        self.config(menu=self.barra_menu)


# ------------------    DECLARACION DE FRAMES    -------------------------

        self.frame_izquierda = FrameIzquierda(master=self)
        self.frame_derecha = FrameLogin(master=self)
        


# ------------------      FRAME IZQUIERDA      ---------------------------


class FrameIzquierda(customtkinter.CTkFrame):
    def __init__(self, master, user:User=None, **kwargs):
        super().__init__(master, **kwargs)
        self.user = user
        self.rows_to_add = self.number_of_buttons()
        row_for_space = 2 + self.rows_to_add
        

        self.grid_rowconfigure(row_for_space, weight=1)
        self.grid(column=0, row=0, sticky='nsew')


        self.imagen = customtkinter.CTkImage(
            dark_image=Image.open(os.path.join(os.getcwd(), 'img', 'logo.png')),
            light_image=Image.open(os.path.join(os.getcwd(), 'img','logo_negro.png')),
            size=(100,100),
            )
        self.label_img = customtkinter.CTkLabel(
            self,
            image=self.imagen, text=''
            )
        
        self.label_img.grid(column=0, row=0)

        self.label_titulo = customtkinter.CTkLabel(
            self,
            text="REVISION",
            )
        
        self.label_titulo.grid(column=0,row=1, pady=20, padx=20)
        

        self.switch_var = customtkinter.StringVar(value='on')
        swich = customtkinter.CTkSwitch(
            self,
            text='Cambiar color',
            command=self.switch_event,
            variable=self.switch_var,
            onvalue='on',
            offvalue='off',
            )
        swich.grid(column=0, row=row_for_space+2, pady=10, padx=10)


        if self.user != None:
            contador = 0
            vistas = VISTAS[self.user.type][self.user.sector]
            for item in vistas:
                for nombre, vista in item.items():
                    contador +=1
                    boton = customtkinter.CTkButton(self, text=nombre, command=self.vista(vista))
                    boton.grid(column=0, row=1+contador, pady=10, padx=10)

            
            self.logout_button = customtkinter.CTkButton(self, text='Logout', command=self.logout)
            self.logout_button.grid(column=0, row=row_for_space+1)


    def base(self, vista):
        self.master.frame_derecha.grid_forget()
        self.master.frame_derecha = vista(master=self.master)
        

    def vista(self, vista):
        return lambda: self.base(vista)


    def logout(self):
        self.master.frame_derecha.grid_forget()
        self.master.frame_izquierda = FrameIzquierda(master=self.master)
        self.master.frame_derecha = FrameLogin(self.master)
        self.master.frame_derecha.usuario_entry.focus_set()
        

    def number_of_buttons(self,):
        if self.user != None:
            contador = 0
            for item in VISTAS[self.user.type][self.user.sector]:
                for _ in item:
                    contador +=1
            return contador
        
        else:
            return 0

    def switch_event(self,) -> None:
        if self.switch_var.get() == 'on':
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")


# ------------------    FRAME LOGIN (DERECHA)   --------------------------


class FrameLogin(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.usuario_obj = None

        self.grid(column=1, row=0, pady=10, padx=10, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,6),weight=1)
        

        self.usuario = customtkinter.StringVar()
        self.usuario_passw = customtkinter.StringVar()


        usuario_label = customtkinter.CTkLabel(self, text='Usuario')
        usuario_label.grid(column=0, row=1)
        
        self.usuario_entry = customtkinter.CTkEntry(self, textvariable=self.usuario)
        self.usuario_entry.grid(column=0, row=2)

        psswd_label = customtkinter.CTkLabel(self, text='Contraseña')
        psswd_label.grid(column=0, row=3)

        psswd_entry = customtkinter.CTkEntry(self, textvariable=self.usuario_passw)
        psswd_entry.grid(column=0, row=4)

        button = customtkinter.CTkButton(self, text='Login', command=self.login)
        button.grid(column=0, row=5, pady=20)

    def login(self, ):
        if self.usuario.get() == '':
            print('no usuario')
        elif self.usuario_passw.get() == '':
            print('no contraseña')
        else:
            usuario_obj = User(self.usuario.get(), self.usuario_passw.get())
            # if usuario_obj.verificar():
            if usuario_obj.is_verificado:
                self.master.frame_izquierda = FrameIzquierda(master=self.master, user=usuario_obj)
                self.master.frame_derecha.grid_forget()
                
            


if __name__ == '__main__':
    app = App()
    app.mainloop()