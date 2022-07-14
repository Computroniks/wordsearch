# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from .GUI import GUI

class App:
    def __init__(self) -> None:
        # We create the root here to give us access to the event loop
        self._root = Tk()
        self._ui = GUI(self._root)
        self._registerEventHandlers()

    def _registerEventHandlers(self) -> None:
        self._root.bind("<<Quit>>", self._quit)

    def _quit(self, *args) -> None:
        self._root.destroy()

    def run(self) -> None:
        self._ui.mainloop()