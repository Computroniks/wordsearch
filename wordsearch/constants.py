# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import platform
import os
import pkgutil
import json


"""Is the current system running macOS?"""
MAC = platform.system() == "Darwin"

"""Is the current system running windows?"""
WIN32 = platform.system() == "Windows"

"""Is the current system running linux?"""
LINUX = platform.system() == "Linux"

"""Base path for settings"""
if MAC:
    BASE_PATH = os.path.join(
        os.path.expanduser("~"),
        "Library/Preferences/wordsearch"
    )
elif WIN32:
    BASE_PATH = "%APPDATA%/wordsearch"
else:
    BASE_PATH = os.path.join(os.path.expanduser("~"), ".wordsearch")

"""Settings filename"""
SETTINGS_NAME = "settings.json"

"""Settings schema"""
_data = pkgutil.get_data(__name__, "schemas/settings.json")
SETTINGS_SCHEMA = json.loads(_data)
