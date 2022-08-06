# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import os
import socket

from wordsearch.constants import BASE_PATH


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

def getMachineIP() -> str:
    """
    getMachineIP Get the IP of this machine

    Gets the current IP of this machine. Uses the system hostname to get
    address so in certain cases this could resolve to 127.0.0.1.
    :return: IP of this machine
    :rtype: str
    """

    return socket.gethostbyname(socket.gethostname())

def loadDefaultsFromSchema(schema: dict) -> dict:
    """
    loadDefaultsFromSchema Loads the defaults from schema

    Parses the provided snippet of the json schema and loads the default
    values of it.

    :param schema: Snippet of schema to parse
    :type schema: dict
    :return: Parsed dict
    :rtype: dict
    """

    # Recursively iterate over dict to extract defaults
    if schema["type"] == "object":
        result = {}
        if "default" in schema:
            return schema["default"]
        for i in schema["properties"]:
            result[i] = loadDefaultsFromSchema(schema["properties"][i])
    elif schema["type"] == "array":
        result = []
        if "default" in schema:
            return schema["default"]
        for i in schema["items"]:
            result.append(loadDefaultsFromSchema(schema["items"]))

    return result

def checkBaseDir() -> None:
    """
    checkBaseDir Ensure base dir exists

    Checks if base directory exists and is accessible for the
    application. If it is not it will be created.
    """

    if os.path.isdir(BASE_PATH):
        return

    os.mkdir(BASE_PATH)
