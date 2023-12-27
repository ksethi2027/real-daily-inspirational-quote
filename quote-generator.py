import random 
from datetime import datetime
import tkinter as tk
import random




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 09:30:15 2023

@author: kashishsethi
"""

print("Welcome to Daily Inspirational Quote Generator!")

quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats"
]

random_quote= random.choice(quotes)
print(random_quote)

# get today's data and format it 
today_date = datetime.now().strftime("%Y-%m-%d")
file_name = f"/Users/kashishsethi/anaconda3/python projectsquote-of-the-day-{today_date}.txt"

# Write the quote to a file 
with open(file_name, 'w') as file:
    file.write(random_quote + "\n")
    
#print("Current working directory:", os.getcwd())
#print("Current file path:", os.path.abspath(__file__))


def display_quote():
    window= tk.Tk()
    window.title("Daily Inspirational Quote")
    window.geometry("400x200")
    
    quote= random.choice(quotes)
    tk.Label(window, text=quote, wraplength=350, justify="center").pack(expand=True)
    window.mainloop()
display_quote()

             
