# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


import random

from .Errors import PuzzleSizeError, OutOfWordsError, RetriesExceededError
from .Word import Word
from ..constants import RETRIES


class Board:
    def __init__(self) -> None:
        """
        __init__ Create instance of board class

        Board class represents the current game board
        """

        self._width: int
        self._height: int
        self._word_count: int
        self._dict: list[str] = []
        self._board: list[list[tuple(Word, int)|None]] = []

    def generate(self, width: int, height: int, dict: list[str], words: int) -> None:
        """
        generate Generate a new board

        Generates a new board from the given parameters

        :param width: Width of board
        :type width: int
        :param height: Height of board
        :type height: int
        :param dict: Dictionary to use for words
        :type dict: list[str]
        :param words: Number of words to put in puzzle
        :type words: int
        """

        self._width = width
        self._height = height
        self._word_count = words
        self._dict = dict

        self._maxWordLen()

        self._board = [[None]*self._width for i in range(self._height)]        

        for i in range(self._word_count):
            self._placeWord()

    def _placeWord(self) -> None:
        """
        _placeWord Place a word on the board

        Chooses a random word from the dictionary and then places the
        word on the board
        """
        retries = 0
        
        while retries < RETRIES:
            retries += 1

            x = random.randint(0, self._width-1)
            y = random.randint(0, self._height-1)
            # True if vertical, false if horizontal
            direction = bool(random.getrandbits(1))
            word = Word(self._chooseWord())
            length = word.length()

            # Make sure end of word is on board
            if direction:
                try:
                    self._board[y+length][x]
                except IndexError:
                    continue
            else:
                try:
                    self._board[y][x+length]
                except IndexError:
                    continue
            
            # Make sure we dont overlap any other words
            if direction:
                for i in range(length):
                    if self._board[y+i][x] is not None:
                        continue
            else:
                for i in range(length):
                    if self._board[y][x+i] is not None:
                        continue

            # Board must be good to populate
            for i in range(length):
                if direction:
                    self._board[y+i][x] = (word, i)
                else:
                    self._board[y][x+i] = (word, i)
            return
        raise RetriesExceededError
            

    def _maxWordLen(self) -> None:
        """
        _maxWordLen Get max word length for specific puzzle size

        Based upon the word count and length of the shortest side.
        """

        shortest_side = min(self._width, self._height)
        min_word_len = (shortest_side // 2)
        self._dict = [word for word in self._dict if len(word) <= min_word_len]

        multiplier = self._word_count / 15 if self._word_count > 15 else 1
        size = int(min_word_len * 2 * multiplier)

        if size > shortest_side:
            raise PuzzleSizeError

        self.printBoard()

    def _chooseWord(self) -> str:
        """
        _chooseWord Chooses a random word from list

        Chooses a random word from the list and then deletes it.

        :return: Chosen word
        :rtype: str
        """ 

        if len(self._dict) < 1:
            raise OutOfWordsError

        index = random.randint(0, len(self._dict)-1)
        return self._dict.pop(index)

    def printBoard(self) -> None:
        """
        printBoard Print board

        Prints the board to stdout
        """

        for i in self._board:
            for j in i:
                if j is None:
                    print("0", end="")
                else:
                    print(j[0]._word[j[1]], end="")
            print()
    