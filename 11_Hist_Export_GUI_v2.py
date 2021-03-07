from tkinter import *
from functools import partial   # To prevent unwanted windows
import re

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        #  In actual program this is blank and is populated with user calculations

        self.all_calc_list = ['5 degrees C is -17.2 degrees F',
                              '6 degrees C is -16.7 degrees F',
                              '7 degrees C is -16.1 degrees F',
                              '8 degrees C is -15.8 degrees F',
                              '9 degrees C is -15.1 degrees F',
                              ]

        # self.all_calc_list = []

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=("Arial", "16", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", "14"),
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)


class History:
    def __init__(self, partner,calc_history):

        background = "a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and
        # 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_history, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)