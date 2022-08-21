# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from typing import Any

import wordsearch.Game.Errors


class Char(str):
    def __init__(self, char: str) -> None:
        """
        __init__ Create instance of Char class

        Char represents a single character in the wordsearch board

        :param char: Character to use. Must have length 1
        :type char: str
        :raises ValueError: Invalid length
        """

        if len(char) != 1:
            raise ValueError("Invalid length. Length of char should be 1.")
        super().__init__()

        self._selected = False
        self._found = False

    def select(self) -> None:
        """
        select Set the char to selected
        """

        self._selected = True
    
    def deselect(self) -> None:
        """
        deselect Set the char to not be selected
        """

        self._selected = False

    def toggleSelect(self) -> bool:
        """
        toggleSelect Toggle the select status

        Toggles the selected status and returns the new value

        :return: New value of selected
        :rtype: bool
        """

        self._selected = not self._selected
        return self._selected

    @property
    def selected(self) -> bool:
        """
        selected Is the char selected?

        Boolean representing if the character represented by the Char
        class is currently selected. True if selected, else false.

        :return: Is the char selected?
        :rtype: bool
        """

        return self._selected

    @selected.setter
    def selected(self, value: Any) -> None:
        """
        selected Setter for selected

        selected should not be set directly, instead the select,
        deselect and toggle methods should be used.

        :param value: Value to set to
        :type value: Any
        :raises wordsearch.Game.Errors.OperationNotPermittedError: Settings
            selected is not permitted
        """
        raise wordsearch.Game.Errors.OperationNotPermittedError(
            "Operation not permitted. You should use the `select`, `deselect` or `toggleSelect` methods instead"
        )

    @property
    def found(self) -> bool:
        """
        found Has the char been found?

        Has the word that this char is a part of been found? True if
        found, else false.

        :return: Is this char marked as found?
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
