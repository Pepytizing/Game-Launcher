# from GameLauncher import *
import tkinter as tk
from tkinter import filedialog
import subprocess


class SampleApp(tk.Tk):
    #global necessary vars
    reihe = 0
    zeile = 1
    names = []
    paths = []
    btns = []

    def __init__(self):
        super().__init__()
        tk.Button(self, text="+", command=self.create_window).grid(row=0, column=0)
        self.file_read()

    def file_append(self):
        """Speichern der Buttoninformationen in einer .txt datei"""
        file = open("Games.txt","a")
        button_name = en_name.get() + "\n"
        button_path = en_origin.get() + "\n"
        file.write(button_name)
        file.write(button_path)
        file.close()

    def file_read(self):
        """Auslesen der gespeicherten Buttoninformationen"""
        file = open("Games.txt", "r")
        global lines
        lines = []
        for zeile in file:
            zeile = zeile.rstrip('\n')
            lines.append(zeile)
        l = len(lines)
        for i in range(l):
            if i % 2 != 0:
                self.startup_buttons(lines[i-1], lines[i])
                self.names.append(lines[i-1])
                self.paths.append(lines[i])
            else:
                pass
        file.close()

    def startup_buttons(self, f_name, f_path):
        """Funktion zum automatischen Erstellen der Buttons aus der Datei beim Starten des Launcher"""
        button = tk.Button(self, text=f_name)
        button.grid(row=self.reihe, column=self.zeile)
        button["command"] = lambda btn=button: self.get_name(btn)
        self.btns.append(button)
        self.position_button()


    def browse(self):
        """Explorer fürs Path auswählen"""
        game = filedialog.askopenfilename(initialdir="C:/", title="choose your file")
        en_origin.set(game)

    def create_window(self):
        """Seperates Fenster mit Entries zum Eingeben der benötigten Informationen für den Button (name & path)"""
        top = tk.Toplevel(self)
        tk.Label(top, text="add a game").grid(row=0)
        tk.Label(top, text="name of the game").grid(row=1)
        tk.Label(top, text="path of the game").grid(row=2)
        global en_name
        en_name = tk.StringVar()
        entry_name = tk.Entry(top, textvariable = en_name)
        entry_name.grid(row=1, column=1)
        global en_origin
        en_origin = tk.StringVar()
        entry_origin = tk.Entry(top, textvariable = en_origin)
        entry_origin.grid(row=2, column=1)
        tk.Button(top, text="...", command=self.browse).grid(row=2, column=2)
        tk.Button(top, text="+ create button", command=self.create_event).grid(row=3, column=2)

    def get_name(self, widget):
        print(widget['text'])
        self.get_id(widget['text'])

    def get_id(self, real_nm):
        """Mithilfe des Namens an den Path des Buttons kommen"""
        length = len(self.btns)
        for i in range(length):
            check_nm = self.btns[i].cget('text')
            if check_nm == real_nm:
                self.game_exec(self.paths[i])
            else:
                print(check_nm)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def position_button(self):
        """Funktion zum automatischem Platzieren der Buttons"""
        if self.zeile < 5:
            self.zeile += 1
        else:
            self.zeile = 0
            self.reihe += 1

    def execu_event(self):
        """Siehe create_event"""
        self.game_exec(en_origin.get())

    def game_exec(self, path):
        """Ausführen der benötigten Datei"""
        self.path = path
        subprocess.call(path)

    def create_event(self):
        """Mithilfe dieser Funktion umgehen wir das Problem, dass entweder zuwenige args genannt werden oder die button_create Funktion zu früh gecallt wird"""
        self.button_create(en_name.get())


    def button_create(self, name):
        """Erstellen unbegrenzt vieler Buttons mithilfe der Informationen aus create_window()"""
        self.name = name
        button = tk.Button(self, text=name)
        button.grid(row=self.reihe, column=self.zeile)
        button["command"] = lambda btn=button: self.get_name(btn)
        self.file_append()
        self.btns.append(button)
        self.names.append(name)
        self.paths.append(en_origin.get())
        self.position_button()


w = SampleApp()
w.mainloop()
