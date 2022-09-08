# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from wordsearch.Settings import Settings
import wordsearch.Game


class WordList:
    def __init__(self, parent: ttk.Frame, settings: Settings, board: wordsearch.Game.Board) -> None:
        """
        __init__ Create the word list

        Create the wordlist that sits to the left hand side of the UI.

        :param parent: Parent frame
        :type parent: ttk.Frame
        :param settings: Instance of application settings
        :type settings: wordsearch.Settings.Settings
        :param board: Instance of game board
        :type board: wordsearch.Game.Board
        """

        self._settings = settings
        self._board = board

        self._frame = ttk.Frame(parent)
        self._frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=0)
        self._frame.rowconfigure(0, weight=0)
        self._frame.rowconfigure(1, weight=1)
        ttk.Separator(self._frame, orient=VERTICAL).grid(column=1, row=0, rowspan=2, padx=5, sticky=(N, S))

        ttk.Label(self._frame, text="Words to find").grid(column=0, row=0, padx=5, pady=5, sticky=(W))
        self._word_list = Text(self._frame, width=30, state=DISABLED)
        self._word_list.grid(column=0, row=1, padx=5, pady=5, sticky=(N, W, S, E))
        self._word_list.tag_config("strikethrough", overstrike=1)

        self._registerEvents()

    def _registerEvents(self) -> None:
        """
        _registerEvents Register event handlers
        """

        self._frame.bind_all("<<LOADED_GAMEBOARD>>", self._loadWords, add='+')
        self._frame.bind_all("<<FOUND_WORD>>", self._loadWords, add="+")

    def _loadWords(self, event: Event) -> None:
        """
        _loadWords Load words

        Load the words into the word list

        :param event: Tkinter event
        :type event: tkinter.Event
        """

        self._word_list.config(state=NORMAL)
        self._word_list.delete(1.0, END)

        for i in self._board.word_list:
            if i.found:
                self._word_list.insert(END, i.word, ("strikethrough"))
            else:
                self._word_list.insert(END, i.word)
            self._word_list.insert(END, "\n")
        self._word_list.config(state=DISABLED)
