# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT


class OperationNotPermittedError(Exception):
    def __init__(
        self,
        message: str = "Operation not permitted"
    ) -> None:
        """
        __init__ Operation not permitted

        :param message: Message to output, defaults to "Operation not
            permitted"
        :type message: str, optional
        """
        
        super().__init__(message)
