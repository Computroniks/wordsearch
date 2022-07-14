# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser

from ..__version__ import __version__, __copyright__, __license__
from ..utils import getRecentFiles

class Window:
    def __init__(self, root: Tk) -> None:
        self._root = root
        self._root.title("Word Search")

        self._dark_theme = StringVar(value=0)
        self._recent_files = getRecentFiles()

        self._root.option_add("*tearOff", FALSE)
        self._createMenu()
    
    def _createMenu(self) -> None:
        self._menubar = Menu(self._root)
        self._root["menu"] = self._menubar

        # Add items
        # File menu
        menu_file = Menu(self._menubar)
        self._menubar.add_cascade(menu=menu_file, label="File")
        menu_file.add_command(label="Save", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_file.add_command(label="Save as", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_file.add_separator()
        menu_file.add_command(label="Load dictionary", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_file.add_command(label="Open word search", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_recent = Menu(menu_file)
        if len(self._recent_files) == 0:
            menu_recent.add_command(label="No recent files", state=DISABLED)
        else:
            for i in self._recent_files:
                menu_recent.add_command(label=os.path.basename(i), command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_file.add_cascade(menu=menu_recent, label="Open recent")
        
        menu_file.add_separator()
        menu_preferences = Menu(menu_file)
        menu_file.add_cascade(menu=menu_preferences, label="Preferences")
        menu_preferences.add_checkbutton(label="Use dark theme?", variable=self._dark_theme, onvalue=1, offvalue=0)
        menu_preferences.add_command(label="Advanced network settings", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_file.add_separator()
        menu_file.add_command(label="Quit", command=lambda :self._root.event_generate("<<Quit>>"))

        # Help
        menu_help = Menu(self._menubar, name="help")
        self._menubar.add_cascade(menu=menu_help, label="Help")
        self._root.createcommand("::tk::mac::ShowHelp", self._showHelp) # macOS help menu
        menu_help.add_command(label="Help", command=self._showHelp)
        menu_help.add_command(label="Online Documentation", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/wiki"))
        menu_help.add_command(label="Release notes", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/releases/"))
        menu_help.add_separator()
        menu_help.add_command(label="View on GitHub", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/"))
        menu_help.add_command(label="Report an issue", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/issues"))
        menu_help.add_command(label="View Licences", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch#licence"))
        menu_help.add_separator()
        menu_help.add_command(label="About", command=self._showInfo)

    def _showHelp(self) -> None:
        messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501")

    def _showInfo(self) -> None:
        message = f"About\nWord Search\nVersion: {__version__}\n{__copyright__}\nLicence: {__license__}"
        messagebox.showinfo(message=message, title="About")

    def mainloop(self) -> None:
        self._root.mainloop()
    