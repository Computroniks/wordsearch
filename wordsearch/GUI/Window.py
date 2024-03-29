# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import os
import webbrowser
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from typing import Any

import wordsearch.Game
from wordsearch.__version__ import __copyright__, __license__, __version__
from wordsearch.GUI.Board import Board
from wordsearch.GUI.ControlSideBar import ControlSideBar
from wordsearch.GUI.WordList import WordList
from wordsearch.Settings import Settings
from wordsearch.constants import HOME
from wordsearch.utils import getRecentFiles


class Window:
    def __init__(self, root: Tk, settings: Settings, game: wordsearch.Game.Board) -> None:
        """
        __init__ Create instace of Window

        Window represents the root window of the GUI although the root
       be passed here first as to ensure that the App can access and
       create events.

        :param root: Root Tk instance
        :type root: Tk
        :param settings: Instance of application settings
        :type settings: wordsearch.Settings.Settings
        :param game: Instance of game to use
        :type game: wordsearch.Game.Board
        """

        self._settings = settings
        self._game = game

        # Configure root
        self._root = root
        self._root.title("Word Search")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

        # Create main frame and configure
        self._mainframe = ttk.Frame(self._root, padding="3 3 12 12")
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._mainframe.columnconfigure(0, weight=0)
        self._mainframe.columnconfigure(1, weight=1)
        self._mainframe.columnconfigure(2, weight=0)
        self._mainframe.rowconfigure(0, weight=1)
        self._control_sidebar = ControlSideBar(self._mainframe, self._settings, self._game)
        self._word_list = WordList(self._mainframe, self._settings, self._game)
        self._board = Board(self._mainframe, self._settings, self._game)

        self._dark_theme = StringVar(
            value=self._settings.settings["display"]["theme"]
        )
        self._dark_theme.trace_add(
            "write",
            self._themeCB
        )

        self._root.option_add("*tearOff", FALSE)
        self._createMenu()
    
    def _createMenu(self) -> None:
        """
        _createMenu Create the menus

        Adds a menubar to root before adding the appropriate cascade
        windows.
        """

        self._menubar = Menu(self._root)
        self._root["menu"] = self._menubar

        # Add items
        # File menu
        menu_file = Menu(self._menubar)
        self._menubar.add_cascade(menu=menu_file, label="File")
        menu_file.add_command(label="Save", command=self._save)
        menu_file.add_command(label="Save as", command=self._saveAs)
        menu_file.add_separator()
        menu_file.add_command(label="Load dictionary", command=self._control_sidebar._selectWordList)
        menu_file.add_command(label="Open word search", command=self._load)
        self._menu_recent = Menu(menu_file)
        menu_file.add_cascade(menu=self._menu_recent, label="Open recent")

        self._populateRecentMenu()
        
        # menu_file.add_separator()
        # menu_preferences = Menu(menu_file)
        # menu_file.add_cascade(menu=menu_preferences, label="Preferences")
        # menu_preferences.add_checkbutton(label="Use dark theme?", variable=self._dark_theme, onvalue="dark", offvalue="light")
        # menu_preferences.add_command(label="Advanced network settings", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))
        menu_file.add_separator()
        menu_file.add_command(label="Quit", command=lambda :self._root.event_generate("<<Quit>>"))

        # Help
        menu_help = Menu(self._menubar, name="help")
        self._menubar.add_cascade(menu=menu_help, label="Help")
        # self._root.createcommand("::tk::mac::ShowHelp", self._showHelp) # macOS help menu
        # menu_help.add_command(label="Help", command=self._showHelp)
        menu_help.add_command(label="Online Documentation", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/wiki"))
        menu_help.add_command(label="Release notes", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/releases/"))
        menu_help.add_separator()
        menu_help.add_command(label="View on GitHub", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/"))
        menu_help.add_command(label="Report an issue", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch/issues"))
        menu_help.add_command(label="View Licences", command=lambda :webbrowser.open("https://github.com/Computroniks/wordsearch#licence"))
        menu_help.add_separator()
        menu_help.add_command(label="About", command=self._showInfo)
        # menu_help.add_command(label="Log", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501"))

    def _populateRecentMenu(self) -> None:
        """
        _populateRecentMenu Populate the recent puzzles menu
        """

        # Clear menu before loading new set
        for i in range(5):
            self._menu_recent.delete(0)

        if len(self._settings.settings["recent"]) == 0:
            self._menu_recent.add_command(label="No recent files", state=DISABLED)
        else:
            for i in self._settings.settings["recent"]:
                self._menu_recent.add_command(label=os.path.basename(i), command=lambda path=i:self._loadDirect(path))

    def _showHelp(self) -> None:
        """
        _showHelp Show the help dialog

        Currently not implemented
        """

        messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501")

    def _showInfo(self) -> None:
        """
        _showInfo Show application info

        Shows the current version and copyright information
        """

        message = f"About\nWord Search\nVersion: {__version__}\n{__copyright__}\nLicence: {__license__}"
        messagebox.showinfo(message=message, title="About")

    def _themeCB(self, *args: Any) -> None:
        """
        _themeCB Callback for theme preference
        """

        self._settings.settings["display"]["theme"] = self._dark_theme.get()
        self._settings.save()
    
    def _save(self) -> None:
        """
        _save Save current board
        """

        # If the board hasn't been saved before or the save file doesn't
        # exist just save as

        if not self._game.loaded:
            messagebox.showwarning(title="No board", message="No board to save")
            return

        if self._game.path == "" or not os.path.exists(self._game.path):
            self._saveAs()
            return

        self._game.save(self._game.path)

    def _saveAs(self) -> None:
        """
        _saveAs Save board as
        """

        if not self._game.loaded:
            messagebox.showwarning(title="No board", message="No board to save")
            return

        filetypes = (
            ("Puzzles", "*.puzzle"),
            ("All files", "*.*")
        )
        path = asksaveasfilename(
            title="Save As",
            initialdir=HOME,
            filetypes=filetypes
        )

        if not isinstance(path, str):
            return

        self._game.save(path)

    def _load(self) -> None:
        """
        _load Load file from disk

        Get user to select file the load it from disk
        """

        filetypes = (
            ("Puzzles", "*.puzzle"),
            ("All files", "*.*")
        )
        path = askopenfilename(
            title="Open",
            initialdir=HOME,
            filetypes=filetypes
        )

        # Update recents list
        if path not in self._settings.settings["recent"]:
            self._settings.settings["recent"].append(path)
            if len(self._settings.settings["recent"]) > 5:
                self._settings.settings["recent"].pop(0)
            self._settings.save()
        self._populateRecentMenu()

        self._loadDirect(path)

    def _loadDirect(self, path: str) -> None:
        """
        _loadDirect Directly load the file

        :param path: Path to file
        :type path: str
        """

        try:
            self._game.load(path)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")
        except:
            messagebox.showerror("Error", "Failed to load save file")
        else:
            self._mainframe.event_generate("<<LOADED_GAMEBOARD>>")

    def mainloop(self) -> None:
        """
        mainloop Start the tkinter main loop
        """
        
        self._root.mainloop()
    