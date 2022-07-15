# SPDX-FileCopyrightText: 2022 Matthew Nickson <mnickson@sidingsmedia.com>
# SPDX-License-Identifier: MIT

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class ControlSideBar:
    def __init__(self, parent: ttk.Frame) -> None:
        """
        __init__ Create the control sidebar

        Create the control sidebar that sits to the right hand side of
        the UI

        :param parent: Parent frame
        :type parent: ttk.Frame
        """

        self._width = IntVar(value=5)
        self._height = IntVar(value=5)
        self._words = IntVar(value=5)
        self._interface_address = StringVar()
        self._listen_port = IntVar(value=59210)
        self._interface_public_key = StringVar()
        self._interface_private_key = StringVar()
        self._peer_address = StringVar()
        self._peer_port = IntVar(value=59211)
        self._public_key = StringVar()
        
        self._frame = ttk.Frame(parent)
        self._frame.grid(column=2, row=0, sticky=(N, W, E, S))
        self._frame.columnconfigure(0, weight=0)
        self._frame.rowconfigure(0, weight=0)
        self._frame.rowconfigure(1, weight=0)
        self._frame.rowconfigure(2, weight=1)
        ttk.Separator(self._frame, orient=VERTICAL).grid(column=0, row=0, rowspan=3, padx=5, sticky=(N, S))

        # Configure puzzle settings
        self._puzzle_settings = ttk.Labelframe(self._frame, text="Puzzle Settings", borderwidth=0)
        self._puzzle_settings.grid(column=1, row=0, pady=10, sticky=(N, W, E))
        self._puzzle_settings.columnconfigure(0, weight=1)
        self._puzzle_settings.columnconfigure(1, weight=1)
        
        ttk.Label(self._puzzle_settings, text="Width").grid(column=0, row=0, sticky=(W))
        ttk.Spinbox(self._puzzle_settings, textvariable=self._width, from_=5, to=20).grid(column=1, row=0, padx=5, pady=5, sticky=(E))

        ttk.Label(self._puzzle_settings, text="Height").grid(column=0, row=1, sticky=(W))
        ttk.Spinbox(self._puzzle_settings, textvariable=self._height, from_=5, to=20).grid(column=1, row=1, padx=5, pady=5, sticky=(E))

        ttk.Label(self._puzzle_settings, text="Number of Words").grid(column=0, row=2, sticky=(W))
        ttk.Spinbox(self._puzzle_settings, textvariable=self._words, from_=5, to=20).grid(column=1, row=2, padx=5, pady=5, sticky=(E))

        ttk.Button(self._puzzle_settings, text="Generate", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501")).grid(column=0, row=3, columnspan=2, sticky=(E, W))

        # Seperator for some visual aid
        ttk.Separator(self._frame, orient=HORIZONTAL).grid(column=1, row=1, columnspan=2, sticky=(E, W))

        # Configure basic network settings
        self._network_settings = ttk.LabelFrame(self._frame, text="Network Settings", borderwidth=0)
        self._network_settings.grid(column=1, row=2, pady=10, sticky=(N, W, E))
        self._network_settings.columnconfigure(0, weight=1)
        self._network_settings.columnconfigure(1, weight=1)

        ttk.Label(self._network_settings, text="Interface").grid(column=0, row=0, columnspan=2, padx=5, pady=5, sticky=(W))

        ttk.Label(self._network_settings, text="Address").grid(column=0, row=1, sticky=(W))
        ttk.Entry(self._network_settings, textvariable=self._interface_address).grid(column=1, row=1, padx=5, pady=5, sticky=(E, W))

        ttk.Label(self._network_settings, text="Listen Port").grid(column=0, row=2, sticky=(W))
        ttk.Spinbox(self._network_settings, textvariable=self._listen_port, from_=1, to=65535).grid(column=1, row=2, padx=5, pady=5, sticky=(E, W))

        ttk.Label(self._network_settings, text="Public Key").grid(column=0, row=3, sticky=(W))
        ttk.Entry(self._network_settings, textvariable=self._interface_public_key).grid(column=1, row=3, padx=5, pady=5, sticky=(E, W))

        ttk.Label(self._network_settings, text="Private Key").grid(column=0, row=4, sticky=(W))
        ttk.Entry(self._network_settings, textvariable=self._interface_private_key).grid(column=1, row=4, padx=5, pady=5, sticky=(E, W))

        ttk.Button(self._network_settings, text="Generate Key Pair", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501")).grid(column=0, row=5, columnspan=2, sticky=(E, W))

        ttk.Label(self._network_settings, text="Peer").grid(column=0, row=6, columnspan=2, padx=5, pady=5, sticky=(W))

        ttk.Label(self._network_settings, text="Endpoint Address").grid(column=0, row=7, sticky=(W))
        ttk.Entry(self._network_settings, textvariable=self._peer_address).grid(column=1, row=7, padx=5, pady=5, sticky=(E, W))

        ttk.Label(self._network_settings, text="Endpoint Port").grid(column=0, row=8, sticky=(W))
        ttk.Spinbox(self._network_settings, textvariable=self._peer_port, from_=1, to=65535).grid(column=1, row=8, padx=5, pady=5, sticky=(E, W))

        ttk.Label(self._network_settings, text="Public Key").grid(column=0, row=9, sticky=(W))
        ttk.Entry(self._network_settings, textvariable=self._public_key).grid(column=1, row=9, padx=5, pady=5, sticky=(E, W))

        ttk.Button(self._network_settings, text="Connect", command=lambda :messagebox.showwarning(message="Sorry, this has not yet been implemented", title="Error 501")).grid(column=0, row=10, columnspan=2, sticky=(E, W))

