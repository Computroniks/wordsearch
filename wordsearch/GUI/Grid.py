# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

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
        self._selected_text = ""

        self.bind("<Configure>", self._resize)
        self.bind("<Button-1>", self._onMouseClick)

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

        for i in range(len(self._board.board)):
            x = org_x
            for j in range(len(self._board.board[i])):
                if self._board.board[i][j].found:
                    self._drawSquare(self._board.board[i][j], x, y, side_length, "light green", f"{j},{i}")
                elif self._board.board[i][j].selected:
                    self._drawSquare(self._board.board[i][j], x, y, side_length, "yellow", f"{j},{i}")
                else:
                    self._drawSquare(self._board.board[i][j], x, y, side_length, "white", f"{j},{i}")    
                x += side_length
            y += side_length

    def _drawSquare(self, letter: str, x: int, y: int, length: int, fill: str, index: str) -> None:
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
        :param fill: Colour to fill rectangle with
        :type fill: str
        :param index: Index of char in board
        :type index: str
        """

        self.create_rectangle(x, y, x+length, y+length, outline="black", fill=fill, tags=index)
        self.create_text(x + (length//2), y + (length//2), text=letter.upper(), tags=index)

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

    def _onMouseClick(self, event: Event) -> None:
        """
        _onMouseClick Callback for mouse button event

        Callback for the left mouse button down event

        :param event: Tkinter event
        :type event: tkinter.Event
        """

        target = self.find_closest(event.x, event.y)

        if target == ():
            # User didn't click on anything
            return
        else: 
            id = target[0]

        x_str, y_str = self.gettags(id)[0].split(",")
        x = int(x_str)
        y = int(y_str)

        if len(self._selected_text) != 0:
            border_present = False

            # BUG: Currently this allows user to select all boxes
            # around a square, i.e can select rectangle instead of line.
            # Implement some form of checking to make sure selection is
            # in a line.

            # Check that the selection is next to a previous one
            borders = [
                (x-1, y),   # Previous
                (x+1, y),   # Next
                (x, y-1),   # Above
                (x, y+1),   # Below
                (x-1, y-1), # Top left
                (x+1, y-1), # Top right
                (x-1, y+1), # Bottom left
                (x+1, y+1), # Bottom right

            ]

            for i in borders:
                try:
                    if self._board.board[i[1]][i[0]].selected:
                        border_present = True
                        break
                except IndexError:
                    continue
            
            if not border_present:
                return

        self._board.board[y][x].select()
        self._selected_text += self._board.board[y][x]

        # Check if user found a word
        found = False
        for i in self._board.word_list:
            if self._selected_text == i.word:
                i.found = True
                found = True
                self.clear()
                for i in self._board.board:
                    for j in i:
                        if j.selected:
                            j.found = True
                
        self.draw()

        # Must emit event after draw
        if found:
            self.event_generate("<<FOUND_WORD>>")

    def clear(self) -> None:
        """
        clear Reset selected text
        """
        
        self._selected_text = ""
    