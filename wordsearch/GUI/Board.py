# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
        self._frame.rowconfigure(1, weight=0)

        self._canvas = Grid(self._frame, self._settings, self._board, background="white")
        self._canvas.grid(column=0, row=0, padx=5, pady=5, sticky=(N, W, S, E))

        ttk.Button(self._frame, text="Clear Selection", command=self._clear).grid(column=0, row=1, sticky=(E, W))

        self._registerEvents()

    def _registerEvents(self) -> None:
        """
        _registerEvents Register event handlers
        """

        self._frame.bind_all("<<LOADED_GAMEBOARD>>", self._drawBoard, add='+')
        self._frame.bind_all("<<FOUND_WORD>>", self._checkWin, add="+")

    def _drawBoard(self, event: Event) -> None:
        """
        _drawBoard Draw the board

        Draws board on canvas

        :param event: Event
        :type event: tkinter.Event
        """

        self._canvas.draw()

    def _clear(self) -> None:
        """
        _clear Clear all selected charaters

        Clears all selected characters and resets the current selected
        string.
        """

        for i in self._board.board:
            for j in i:
                j.deselect()

        self._canvas.clear()
        self._canvas.draw()

    def _checkWin(self, event: Event) -> None:
        """
        _checkWin Check if player has won

        Checks if the player has won. If so, show a message box with
        congratulations.

        :param event: Unused tkinter event
        :type event: tkinter.Event
        """
        
        if self._board.checkWin():
            messagebox.showinfo(
                title="Complete",
                message="Congratulations, you completed the wordsearch. Well done!"
            )
