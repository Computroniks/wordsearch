# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk


class Grid(Canvas):
    def __init__(self, parent, **kwargs) -> None:
        """
        __init__ Create instance of Grid

        Grid represents the canvas on which to draw the game board.

        :param parent: Parent widget
        :type parent: any
        """ 
        super().__init__(parent, **kwargs)
    