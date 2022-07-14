# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from .Game import Board

def initConn(ip: str, port: int, timeout: int) -> bool:
    pass

def sendBoard(board: Board, timeout: int) -> bool:
    pass

def listen(callback: function) -> None:
    pass