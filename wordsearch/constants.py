# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import json
import os
import pkgutil
import platform

MAC = platform.system() == "Darwin"
"""Is the current system running macOS?"""

WIN32 = platform.system() == "Windows"
"""Is the current system running windows?"""

LINUX = platform.system() == "Linux"
"""Is the current system running linux?"""

HOME = os.path.expanduser("~")
"""Path to users home directory"""

if MAC:
    BASE_PATH = os.path.join(
        HOME,
        "Library/Preferences/wordsearch"
    )
    """Base path for settings"""
elif WIN32:
    appdata = os.getenv("APPDATA")
    BASE_PATH = os.path.join(appdata, "wordsearch")
    """Base path for settings"""
else:
    BASE_PATH = os.path.join(HOME, ".wordsearch")
    """Base path for settings"""


SETTINGS_NAME = "settings.json"
"""Settings filename"""

_data = pkgutil.get_data(__name__, "schemas/settings.json")
SETTINGS_SCHEMA = json.loads(_data)
"""Settings schema"""

RETRIES = 5
"""Number of attempts made to place a word"""

ALPHABET = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"

]
"""Upper case alphabet"""
