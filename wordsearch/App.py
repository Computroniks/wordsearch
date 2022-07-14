# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from .GUI import GUI

class App:
    def __init__(self) -> None:
        """
        __init__ Create instance of App

        App provides the entrypoint to the game and controls all aspects
        of it.
        """

        # We create the root here to give us access to the event loop
        self._root = Tk()
        self._ui = GUI(self._root)
        self._registerEventHandlers()

    def _registerEventHandlers(self) -> None:
        """
        _registerEventHandlers Register the event handlers

        Register the handlers for custom events
        """

        self._root.bind("<<Quit>>", self._quit)

    def _quit(self, *args) -> None:
        """
        _quit Destroy all windows and quit the application
        """

        self._root.destroy()

    def run(self) -> None:
        """
        run Start the tkinter main loop
        """
        
        self._ui.mainloop()