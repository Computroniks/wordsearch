# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from .App import App

assert len( __package__ ) > 0, """
The '__main__' module does not seem to have been run in the context of a
runnable package ... did you forget to add the '-m' flag?
Usage: python3 -m wordsearch
"""

def main() -> None:
    app = App()
    app.run()

if __name__ == "__main__":
    main()
