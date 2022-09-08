# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import wordsearch.Game.Errors

# TODO: Make Word child of str like Char


class Word:
    def __init__(self, word: str) -> None:
        """
        __init__ Create instance of word

        Represents each word that is on the board

        :param word: Word to represent
        :type word: str
        """
        
        self._word = word
        self._found = False

    def length(self) -> int:
        """
        length Get length of word

        :return: Length of the word
        :rtype: int
        """

        return len(self._word)

    @property
    def word(self) -> str:
        """
        word String representation of word
        :return: Word
        :rtype: str
        """

        return self._word

    @word.setter
    def word(self, value) -> None:
        """
        word Set word 

        :raises wordsearch.Game.Errors.OperationNotPermittedError: Operation
            not permitted
        """
        raise wordsearch.Game.Errors.OperationNotPermittedError

    @property
    def found(self) -> bool:
        """
        found Has this word been found

        Has the word represented by this class been found by the user.
        True if found, else false.

        :return: Has the word been found
        :rtype: bool
        """

        return self._found

    @found.setter
    def found(self, value: bool) -> None:
        """
        found Setter for found

        :param value: Value to set
        :type value: bool
        """
        
        self._found = bool(value)
    