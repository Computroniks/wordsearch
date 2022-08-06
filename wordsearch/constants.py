# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import json
import os
import pkgutil
import platform

"""Is the current system running macOS?"""
MAC = platform.system() == "Darwin"

"""Is the current system running windows?"""
WIN32 = platform.system() == "Windows"

"""Is the current system running linux?"""
LINUX = platform.system() == "Linux"

"""Path to users home directory"""
HOME = os.path.expanduser("~")

"""Base path for settings"""
if MAC:
    BASE_PATH = os.path.join(
        HOME,
        "Library/Preferences/wordsearch"
    )
elif WIN32:
    BASE_PATH = "%APPDATA%/wordsearch"
else:
    BASE_PATH = os.path.join(HOME, ".wordsearch")

"""Settings filename"""
SETTINGS_NAME = "settings.json"

"""Settings schema"""
_data = pkgutil.get_data(__name__, "schemas/settings.json")
SETTINGS_SCHEMA = json.loads(_data)

"""Number of attempts made to place a word"""
RETRIES = 5
