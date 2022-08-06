# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from wordsearch.Settings import Settings


class Grid(Canvas):
    def __init__(self, parent, settings: Settings, **kwargs) -> None:
        """
        __init__ Create instance of Grid

        Grid represents the canvas on which to draw the game board.

        :param parent: Parent widget
        :type parent: any
        :param settings: Instance of application settings
        :type settings: Settings
        """ 
        super().__init__(parent, **kwargs)

        self._settings = settings
    