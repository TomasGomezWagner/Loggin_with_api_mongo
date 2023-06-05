import customtkinter

class FrameFiltratImg(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(column=1, row=0, pady=10, padx=10, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((7), weight=1)

        self.ruta_descarte  = customtkinter.StringVar()
        self.ruta_img       = customtkinter.StringVar()

        self.subtitulo = customtkinter.CTkLabel(
            self,
            text='FILTRAR IMAGENES'
            )
        self.subtitulo.grid(column=0, row=0, pady=10, padx=10, sticky='ew')

        self.label_txt = customtkinter.CTkLabel(
            self,
            text='Ruta del archivo de descartes',
            anchor='w'
            )
        self.label_txt.grid(column=0, row=1)

        self.entry_ruta_txt_descarte = customtkinter.CTkEntry(
            self, 
            textvariable=self.ruta_descarte
            )
        self.entry_ruta_txt_descarte.grid(column=0, row=2, pady=(10,5), padx=20, sticky='ew')

        self.btn_examinar = customtkinter.CTkButton(
            self,
            text='EXAMINAR', 
            
            )
        self.btn_examinar.grid(column=0, row=3, pady=(5,10), padx=50, sticky='ew')

        self.label_txt = customtkinter.CTkLabel(
            self,
            text='Ruta de la carpeta de imagenes', 
            anchor='w'
            )
        self.label_txt.grid(column=0, row=4, pady=(30,0))
        
        self.entry_ruta = customtkinter.CTkEntry(
            self,
            textvariable=self.ruta_img
            )
        self.entry_ruta.grid(column=0, row=5, pady=(10,5), padx=20, sticky='ew')

        self.btn_examinar_carpeta = customtkinter.CTkButton(
            self,
            text='EXAMINAR',
            
            )
        self.btn_examinar_carpeta.grid(column=0, row=6, pady=(5,10), padx=50, sticky='ew')

        self.btn_procesar = customtkinter.CTkButton(
            self,
            text='PROCESAR',
            
        )
        self.btn_procesar.grid(column=0, row=8, pady=20, padx=20, sticky='ew')