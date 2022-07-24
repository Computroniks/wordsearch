# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

import os
import json

from .constants import BASE_PATH, SETTINGS_NAME, SETTINGS_SCHEMA
from .utils import getMachineIP, loadDefaultsFromSchema, checkBaseDir


class Settings:
    def __init__(self) -> None:
        self.settings: dict
        self._load()

    def _initialSettings(self) -> None:
        """
        _initialSettings Initial settings configuration

        Check if settings file exists and if not creates it and populates it
        with the default information from the schema
        """

        checkBaseDir()

        if os.path.isfile(os.path.join(BASE_PATH, SETTINGS_NAME)):
            return

        self.settings = loadDefaultsFromSchema(SETTINGS_SCHEMA)
        self.settings["network"]["interface"]["address"] = getMachineIP()

        self.save()
        
    def save(self) -> None:
        """
        save Save settings

        Save any changes that were made to the settings.
        """
        
        # Save file
        with open(os.path.join(BASE_PATH, SETTINGS_NAME), "w") as f:
            json.dump(self.settings, f, indent=4) # Indent to make manual editing easier

    def _load(self) -> None:
        """
        loadSettings Load the application settings

        Loads the application settings from APPDATA or equivalent

        :return: Read and parsed settings
        :rtype: dict
        """

        self._initialSettings()

        with open(os.path.join(BASE_PATH, SETTINGS_NAME), "r") as f:
            self.settings = json.load(f)
