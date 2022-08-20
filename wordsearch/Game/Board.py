# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import pickle
import random

from wordsearch.constants import RETRIES, ALPHABET
import wordsearch.Game.Errors
from wordsearch.Game.Word import Word


class Board:
    def __init__(self) -> None:
        """
        __init__ Create instance of board class

        Board class represents the current game board
        """

        self._width: int = 1
        self._height: int = 1
        self._word_count: int = 0
        self._dict: list[str] = []
        self._board: list[list[(Word, int)|None]] = []
        self._word_list: list[Word] = []
        self.path: str = ""
        self.loaded = False

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
        self._word_list = []

        self._board = [[None]*self._width for i in range(self._height)]        
        
        # Place words
        for i in range(self._word_count):
            self._placeWord()

        # Fill empty spaces
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] is None:
                    self._board[i][j] = self._getChar()

        self.path = ""
        self.loaded = True

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
            
            self._word_list.append(word)
            return
        raise wordsearch.Game.Errors.RetriesExceededError

    def _chooseWord(self) -> str:
        """
        _chooseWord Chooses a random word from list

        Chooses a random word from the list and then deletes it.

        :return: Chosen word
        :rtype: str
        """ 

        if len(self._dict) < 1:
            raise wordsearch.Game.Errors.OutOfWordsError

        index = random.randint(0, len(self._dict)-1)
        return self._dict.pop(index)

    def _getChar(self) -> str:
        """
        _getChar Get a random character

        Gets a random character

        :return: A random character
        :rtype: str
        """

        # TODO: Make this return chars based on frequency in english
        # language. I.e e more frequent than z

        return random.choice(ALPHABET)


    def printBoard(self) -> None:
        """
        printBoard Print board

        Prints the board to stdout
        """

        for i in self._board:
            for j in i:
                if not isinstance(j, tuple):
                    print("0", end="")
                else:
                    print(j[0].word[j[1]], end="")
            print()

    def save(self, path: str) -> None:
        """
        save Save the board to disk

        Saves the board and wordlist to disk

        :param path: Path to save to
        :type path: str
        """

        self.path = str(path)
        data = [self._board, self._word_list, self._width, self._height]
        with open(path, "wb") as f:
            pickle.dump(data, f)

    def load(self, path: str) -> None:
        """
        load Load puzzle from disk

        Load the puzzle data from disk and parse it before storing it.

        :param path: _description_
        :type path: str
        """
        with open(path,"rb") as f:
            data = pickle.load(f)
        # Load to local variables first to check for exceptions.
        # Prevents partial load of board
        board = data[0]
        word_list = data[1]
        width = data[2]
        height = data[3]
        self._board = board
        self._word_list = word_list
        self._width = width
        self._height = height
        self.loaded = True

    @property
    def width(self) -> int:
        """
        width Width of board

        :return: Width
        :rtype: int
        """

        return self._width

    @width.setter
    def width(self, value) -> None:
        """
        width Set width of board

        :raises wordsearch.Game.Errors.OperationNotPermittedError: Operation
            not permitted
        """
        raise wordsearch.Game.Errors.OperationNotPermittedError

    @property
    def height(self) -> int:
        """
        height height of board

        :return: Height
        :rtype: int
        """

        return self._height

    @height.setter
    def height(self, value) -> None:
        """
        height Set height of board

        :raises wordsearch.Game.Errors.OperationNotPermittedError: Operation
            not permitted
        """
        raise wordsearch.Game.Errors.OperationNotPermittedError

    @property
    def board(self) -> list[list[(Word, int)]]:
        """
        board 2D array of board

        :return: Board
        :rtype: list[list[tuple(Word, int)|None]]
        """

        return self._board

    @board.setter
    def board(self, value) -> None:
        """
        board Set board

        :raises wordsearch.Game.Errors.OperationNotPermittedError: Operation
            not permitted
        """
        raise wordsearch.Game.Errors.OperationNotPermittedError

    @property
    def word_list(self) -> list[Word]:
        """
        word_list Array representing words to find

        :return: Word list
        :rtype: list[Word]
        """

        return self._word_list

    @word_list.setter
    def word_list(self, value) -> None:
        """
        word_list Set word list

        :raises wordsearch.Game.Errors.OperationNotPermittedError: Operation
            not permitted
        """
        raise wordsearch.Game.Errors.OperationNotPermittedError
    