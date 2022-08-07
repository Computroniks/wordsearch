# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


class PuzzleSizeError(Exception):
    def __init__(
        self,
        message: str = "Puzzle is too small for number of words"
    ) -> None:
        """
        __init__ The puzzle size is too small for the number of words

        :param message: Message to output, defaults to "Puzzle is too
            small for number of words"
        :type message: str, optional
        """
        
        super().__init__(message)
