# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from .Grid import Grid
from ..Settings import Settings


class Board:
    def __init__(self, parent: ttk.Frame, settings: Settings) -> None:
        """
        __init__ Create the board

        Create the board that sits in the centre of the UI

        :param parent: Parent frame
        :type parent: ttk.Frame
        :param settings: Instance of application settings
        :type settings: Settings
        """

        self._settings = settings

        self._frame = ttk.Frame(parent)
        self._frame.grid(column=1, row=0, sticky=(N, W, S, E))
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

        self._canvas = Grid(self._frame, self._settings, background="white")
        self._canvas.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W, S, E))
    