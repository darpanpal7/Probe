# ===================================================================================================
# IMPORTS

""" 1. 'os' for accessing file system and hard drives
    2. 'sys' for creating gui windows
    3. 'datetime' to monitor execution speed
    4. 'tkinter' for creating gui
    5. 'threading' for multithreading
    5. 'script' is the other file
"""

import os
import sys
from datetime import datetime
import tkinter as tk
import tkinter.ttk as ttk
from threading import Thread
from script import SearchScript
py3 = True

# ===================================================================================================
# GUI CLASS


class TopLevel:

    s = None

    def callS(self):
        self.s = SearchScript()

    # ------------------------------------------------------------------------------------------
    # INITIAL CONSTRUCTOR

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        Thread(target=self.callS).start()  # creating seprate thread

        _bgcolor = '#d9d9d9'   # X11 color: 'gray85'
        _fgcolor = '#000000'   # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[
                       ('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1366x685")
        top.state("zoomed")
        top.minsize(120, 120)
        top.maxsize(1370, 729)
        top.resizable(1, 1)
        top.title("Search")
        top.iconbitmap("Icons\\icon.ico")
        top.configure(background="#c0c0c0")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

    # Canvas options
    # ___________________________________________________________________________________________________

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.0, rely=0.058,
                           relheight=0.879, relwidth=0.998)

        self.Canvas1.configure(background="#ffffff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")

    # Text options
    # ___________________________________________________________________________________________________

        self.Text1 = tk.Text(self.Canvas1, wrap="none")
        self.Text1.place(relx=0.007, rely=0.05,
                         relheight=0.905, relwidth=0.982)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(relief="raised")
        self.Text1.configure(cursor="xterm")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.scrollbar = tk.Scrollbar(self.Canvas1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.configure(command=self.Text1.yview)

        self.Text1.configure(yscrollcommand=self.scrollbar.set)

    # Menu options
    # ___________________________________________________________________________________________________

        self.menubar = tk.Menu(top, font="TkMenuFont",
                               bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 hidemargin=1,
                                 label="File")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="New Search Window")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Open File List")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Close File List",
            state="disabled")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Close")
        self.sub_menu.add_separator(
            background="#d9d9d9")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Export")
        self.sub_menu.add_separator(
            background="#d9d9d9")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Exit",
            command=top.destroy)
        self.sub_menu1 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="Edit")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Cut",
            state="disabled")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Copy",
            state="disabled")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Paste",
            state="disabled")
        self.sub_menu1.add_separator(
            background="#d9d9d9")
        self.sub_menu1.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Select All")
        self.sub_menu1.add_separator(
            background="#d9d9d9")
        self.sub_menu12 = tk.Menu(top, tearoff=0)
        self.sub_menu1.add_cascade(menu=self.sub_menu12,
                                   activebackground="#ececec",
                                   activeforeground="#000000",
                                   background="#d9d9d9",
                                   font="TkMenuFont",
                                   foreground="#000000",
                                   label="Advanced")
        self.sub_menu12.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Copy to folder")
        self.sub_menu12.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="Move to folder")
        self.sub_menu123 = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu123,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 font="TkMenuFont",
                                 foreground="#000000",
                                 label="Help")
        self.sub_menu123.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            font="TkMenuFont",
            foreground="#000000",
            label="About Search")

    # Label options
    # ___________________________________________________________________________________________________

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.007, rely=0.949, height=24, width=500)

        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Items''')
        tooltip_font = "TkDefaultFont"

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.625, rely=0.949, height=24, width=500)

        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''State''')
        tooltip_font = "TkDefaultFont"

    # Entry options
    # ___________________________________________________________________________________________________

        self.SearchEntry = tk.Entry(top)
        self.SearchEntry.place(relx=0.007, rely=0.015,
                               height=20, relwidth=0.772)

        self.SearchEntry.configure(background="white")
        self.SearchEntry.configure(disabledforeground="#a3a3a3")
        self.SearchEntry.configure(font="TkFixedFont")
        self.SearchEntry.configure(foreground="#000000")
        self.SearchEntry.configure(highlightbackground="#d9d9d9")
        self.SearchEntry.configure(highlightcolor="black")
        self.SearchEntry.configure(insertbackground="black")
        self.SearchEntry.configure(selectbackground="#c4c4c4")
        self.SearchEntry.configure(selectforeground="black")

    # Button options
    # ___________________________________________________________________________________________________

        self.SearchButton = tk.Button(top)
        self.SearchButton.place(relx=0.791, rely=0.015, height=24, width=277)

        self.SearchButton.configure(activebackground="#ececec")
        self.SearchButton.configure(activeforeground="#000000")
        self.SearchButton.configure(background="#ffffff")
        self.SearchButton.configure(disabledforeground="#a3a3a3")
        self.SearchButton.configure(foreground="#000000")
        self.SearchButton.configure(highlightbackground="#d9d9d9")
        self.SearchButton.configure(highlightcolor="black")
        self.SearchButton.configure(pady="0")
        self.SearchButton.configure(text='''Search''')
        self.SearchButton.configure(command=self.search)

# BEHAVIOUR METHODS
# ------------------------------------------------------------------------------------------------------

    def create_items(self, file_list):
        """ Function that takes a list and creates button for each item """

        for each in file_list:
            b = tk.Button(self.Text1, text="%s" %
                          each)  # adding text to button
            b.pack(side=tk.LEFT)
            b.configure(relief="flat")
            # command to startfile
            b.configure(command=lambda x=each: self.startfile(x))
            self.Text1.window_create("end", window=b)
            self.Text1.insert("end", "\n")

        # disabling the textbox to avoid further changes made by the user
        self.statechangetextbox(0)

    def modifyrightlabel(self, var):
        """ Function to modify text in Right Label """

        self.Label2.configure(text=var)

    def modifyleftlabel(self, var):
        """ Function to modify text in Left Label """

        self.Label1.configure(text=var)

    def statechangetextbox(self, var):
        """ Function to change state of TextBox """

        if var:
            self.Text1.configure(state="normal")
        else:
            self.Text1.configure(state="disabled")

    def cleartextbox(self):
        """ Function to clear the TextBox """

        self.Text1.delete(1.0, tk.END)

    def getentry(self):
        """ Function to get text in the EntryBox """

        return self.SearchEntry.get().lower()

    def startfile(self, var):
        """ Funtion to open the file or folder """

        if var.endswith("_"):
            var = var.rstrip("_")  # to delete the trailing "_" from the path
        os.startfile(var)

    def search(self):
        """ Function to get the search keyword and search in the dictionary and provide results to the gui window """

        # taking input
        var = self.getentry()
        if var == "":  # if empty string do not search
            return

        self.modifyrightlabel("Searching...")
        self.statechangetextbox(1)
        self.cleartextbox()

        t1 = datetime.now()
        print("File to search : ", var)
        file_list = self.s.do_search(var)

        total_files = len(file_list)  # list of total matched files and folders
        file_list.sort()  # sorting files

        self.create_items(file_list)

        # output on terminal window
        print("Total file : ", total_files)
        t2 = datetime.now()
        total_time = t2 - t1
        print("Time Taken : ", total_time)

        # output on gui window
        labelstring = "Total Files : " + \
            str(total_files) + ",     Total Time : " + str(total_time)
        self.modifyleftlabel(str(labelstring))
        self.modifyrightlabel("Search Complete.")

# ===================================================================================================
