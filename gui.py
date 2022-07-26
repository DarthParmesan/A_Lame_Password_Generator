from tkinter import *
from tkinter import ttk
from pwd_generator import *

class gui:

    def __init__(self):
        self.root = Tk()
        self.pg = pwd_generator()
        self.root.title("ALPG v1.1")

        win_width = 300
        win_height = 400

        scr_width = self.root.winfo_screenwidth()
        scr_height = self.root.winfo_screenheight()

        center_x = int(scr_width / 2 - win_width / 2)
        center_y = int(scr_height / 2 - win_height / 2)

        # ==== Colors ====
        m1c = '#00ee00'
        bgc = '#222222'
        dbg = '#000000'
        fgc = '#111111'

        self.root.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc, activeForeground=bgc,
                          highlightColor=m1c, highlightBackground=m1c)

        self.root.geometry(f"{win_width}x{win_height}+{center_x}+{center_y}")
        self.root.resizable(0, 0)
        self.init_widgets()

    def run(self):
        self.root.mainloop()

    def init_widgets(self):
        options = ["8", "10", "12"]
        font = "Courier 12 bold"
        self.selection = IntVar()
        self.selection.set(options[0])

        Label(self.root, text="A Lame Password Generator", font="Arial 14 bold").place(x=12, y=15)

        ttk.Separator(self.root, orient='horizontal').place(x=0, y=50, relwidth=1)

        Label(self.root, text="Random Password", font="Arial 10 bold").place(x=20, y=60)
        Label(self.root, text="Password Length: ").place(x=20, y=90)
        OptionMenu(self.root, self.selection, *options).place(x=120, y=85)
        Button(self.root, text="Generate", command=self.output_random_pwd).place(x=190, y=87)
        Label(self.root, text="Your Password: ").place(x=20, y=130)
        self.random_output = Text(self.root, width=20, height=1, font="Arial 10")
        self.random_output.place(x=110, y=130)

        ttk.Separator(self.root, orient='horizontal').place(x=0, y=160, relwidth=1)

        Label(self.root, text="Verb-Noun Password", font="Arial 10 bold").place(x=20, y=170)
        Button(self.root, text="Generate", command=self.output_nv_password).place(x=20, y=200)
        Label(self.root, text="Your Password: ").place(x=20, y=240)
        self.nv_output = Text(self.root, width=20, height=1, font="Arial 10")
        self.nv_output.place(x=110, y=240)

        ttk.Separator(self.root, orient='horizontal').place(x=0, y=280, relwidth=1)

        Label(self.root, text="Country Name Password", font="Arial 10 bold").place(x=20, y=290)
        Button(self.root, text="Generate", command=self.output_country_pwd).place(x=20, y=320)
        Label(self.root, text="Your Password: ").place(x=20, y=360)
        self.country_pwd_output = Text(self.root, width=20, height=1, font="Arial 10")
        self.country_pwd_output.place(x=110, y=360)

    def output_random_pwd(self):
        self.random_output.delete(1.0, END)
        self.random_output.insert(END, self.pg.random_password(self.selection.get()))

    def output_nv_password(self):
        self.nv_output.delete(1.0, END)
        self.nv_output.insert(END, self.pg.leet_password())

    def output_country_pwd(self):
        self.country_pwd_output.delete(1.0, END)
        self.country_pwd_output.insert(END, self.pg.country_name_password())