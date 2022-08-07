# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


class OutOfWordsError(Exception):
    def __init__(
        self,
        message: str = "Dictionary does not have enough words to complete generation"
    ) -> None:
        """
        __init__ The process has ran out of words to use

        :param message: Message to output, defaults to "Dictionary does
            not have enough words to complete generation"
        :type message: str, optional
        """
        
        super().__init__(message)
