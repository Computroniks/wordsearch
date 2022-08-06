# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


class Word:
    def __init__(self, word: str) -> None:
        """
        __init__ Create instance of word

        Represents each word that is on the board

        :param word: Word to represent
        :type word: str
        """
        
        self._word = word

    def length(self) -> int:
        """
        length Get length of word

        :return: Length of the word
        :rtype: int
        """

        return len(self._word)
    