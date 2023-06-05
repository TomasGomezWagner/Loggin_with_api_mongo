import customtkinter

class FrameFiltratTxt(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid(column=1, row=0, pady=10, padx=10, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.ruta_txt = customtkinter.StringVar()

        self.subtitulo = customtkinter.CTkLabel(
            self,
            text='FILTRAR ARCHIVO'
            )
        self.subtitulo.grid(column=0, row=0, pady=10, padx=10, sticky='ew')

        self.entry_ruta = customtkinter.CTkEntry(
            self,
            textvariable=self.ruta_txt
            )
        self.entry_ruta.grid(column=0, row=2, pady=20, padx=20, sticky='ew')

        self.btn_examinar = customtkinter.CTkButton(
            self,
            text='EXAMINAR',
            
            )
        self.btn_examinar.grid(column=0, row=3, pady=20, padx=50, sticky='ew')

        self.btn_procesar = customtkinter.CTkButton(
            self,
            text='PROCESAR',
            
            )
        self.btn_procesar.grid(column=0, row=5, pady=20, padx=20, sticky='ew')
