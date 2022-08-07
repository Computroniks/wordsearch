# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk

from wordsearch.Settings import Settings


class WordList:
    def __init__(self, parent: ttk.Frame, settings: Settings) -> None:
        """
        __init__ Create the word list

        Create the wordlist that sits to the left hand side of the UI.

        :param parent: Parent frame
        :type parent: ttk.Frame
        :param settings: Instance of application settings
        :type settings: wordsearch.Settings.Settings
        """

        self._settings = settings

        self._frame = ttk.Frame(parent)
        self._frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self._frame.columnconfigure(0, weight=1)
        self._frame.columnconfigure(1, weight=0)
        self._frame.rowconfigure(0, weight=0)
        self._frame.rowconfigure(1, weight=1)
        ttk.Separator(self._frame, orient=VERTICAL).grid(column=1, row=0, rowspan=2, padx=5, sticky=(N, S))

        ttk.Label(self._frame, text="Words to find").grid(column=0, row=0, padx=5, pady=5, sticky=(W))
        self._word_list = Text(self._frame, width=30, state=DISABLED).grid(column=0, row=1, padx=5, pady=5, sticky=(N, W, S, E))
