# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from wordsearch.GUI.Grid import Grid
from wordsearch.Settings import Settings
import wordsearch.Game

class Board:
    def __init__(self, parent: ttk.Frame, settings: Settings, board: wordsearch.Game.Board) -> None:
        """
        __init__ Create the board

        Create the board that sits in the centre of the UI

        :param parent: Parent frame
        :type parent: ttk.Frame
        :param settings: Instance of application settings
        :type settings: wordsearch.Settings.Settings
        :param board: Board class
        :type board: wordsearch.Game.Board
        """

        self._settings = settings
        self._board = board

        self._frame = ttk.Frame(parent)
        self._frame.grid(column=1, row=0, sticky=(N, W, S, E))
        self._frame.columnconfigure(0, weight=1)
        self._frame.rowconfigure(0, weight=1)

        self._canvas = Grid(self._frame, self._settings, self._board, background="white")
        self._canvas.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W, S, E))

        self._registerEvents()

    def _registerEvents(self) -> None:
        """
        _registerEvents Register event handlers
        """

        self._frame.bind_all("<<LOADED_GAMEBOARD>>", self._drawBoard, add='+')

    def _drawBoard(self, event: Event) -> None:
        """
        _drawBoard Draw the board

        Draws board on canvas

        :param event: Event
        :type event: tkinter.Event
        """

        self._canvas.draw()
