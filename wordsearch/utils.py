# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

def loadFile(path: str) -> list[str]:
    pass

def getRecentFiles() -> list[str]:
    """
    getRecentFiles Get a list of recent files

    Retrieves the list of recently opened files from application data
    and returns them. Maximum length of returned list is 5 items.

    :return: List of files
    :rtype: list[str]
    """
    
    # Just return some test data for now
    data = [
        "/home/usr/test.puzzle",
        "/home/usr/test2.puzzle",
        "/home/usr/test3.puzzle",
        "/home/usr/test4.puzzle"
    ]
    return data
