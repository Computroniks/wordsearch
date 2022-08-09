# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk
from wordsearch.Game.Word import Word

from wordsearch.Settings import Settings
import wordsearch.Game


class Grid(Canvas):
    def __init__(
        self,
        parent,
        settings: Settings,
        board: wordsearch.Game.Board,
        **kwargs
    ) -> None:
        """
        __init__ Create instance of Grid

        Grid represents the canvas on which to draw the game board.

        :param parent: Parent widget
        :type parent: any
        :param settings: Instance of application settings
        :type settings: wordsearch.Settings.Settings
        :param board: Current game board
        :type board: wordsearch.Game.Board
        """ 
        super().__init__(parent, **kwargs)

        self._settings = settings
        self._board = board
        self._width = self.winfo_width()
        self._height = self.winfo_height()

        self.bind("<Configure>", self._resize)

    def draw(self) -> None:
        """
        draw Draw the board to the screen

        Draws and scales the current game board onto the canvas
        """

        # Clear the canvas
        self.delete("all")

        width = self.winfo_width()
        height = self.winfo_height()

        bwidth = self._board.width
        bheight = self._board.height

        # 10px padding on all sides of grid
        width -= 20
        height -= 20

        # Get smallest scale factor
        side_length = min(width // bwidth, height // bheight)
        # Center grid
        org_x = ((width - (side_length*bwidth)) // 2) + 10
        y = ((height - (side_length*bheight)) // 2) + 10

        for i in self._board.board:
            x = org_x
            for j in i:
                if isinstance(j, tuple):
                    letter = j[0].word[j[1]]
                else:
                    letter = j
                self._drawSquare(letter, x, y, side_length)
                x += side_length
            y += side_length

    def _drawSquare(self, letter: str, x: int, y: int, length: int) -> None:
        """
        _drawSquare Draw individual grid square

        Draws an individual grid square at given position.

        :param letter: Letter to put in square
        :type letter: str
        :param x: X coordinate
        :type x: int
        :param y: Y coordinate
        :type y: int
        :param length: Side length
        :type length: int
        """

        self.create_rectangle(x, y, x+length, y+length, outline="black")
        self.create_text(x + (length//2), y + (length//2), text=letter.upper())

    def _resize(self, event: Event) -> None:
        """
        _resize Callback for resize event

        Check if we have actually resized before handling event

        :param event: Tkinter event
        :type event: tkinter.Event
        """

        changed = self._width != event.width or self._height != event.height
        if not changed:
            return
        
        self.draw()



    