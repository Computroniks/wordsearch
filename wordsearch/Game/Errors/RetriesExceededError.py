# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


class RetriesExceededError(Exception):
    def __init__(
        self,
        message: str = "Puzzle generation retries exceeded"
    ) -> None:
        """
        __init__ Failed to generate puzzle

        :param message: Message to output, defaults to "Puzzle
            generation retries exceeded"
        :type message: str, optional
        """
        
        super().__init__(message)
