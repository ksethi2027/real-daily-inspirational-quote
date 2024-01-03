import random 
from datetime import datetime
import tkinter as tk
import random
from openai import OpenAI 
import os
from dotenv import load_dotenv


def display_quote(quote):
    window = tk.Tk()
    window.title("Daily Inspirational Quote")
    window.geometry("600x300")  # Adjust the size as needed
    window.configure(bg="ivory2")

    # Splitting quote and author if needed
    # Assuming quote format is "quote text - author"
    if " - " in quote:
        quote_text, author = quote.split(" - ")
    else:
        quote_text = quote
        author = ""

    quote_label = tk.Label(window, text=quote_text, wraplength=550, justify="center", font=("Arial", 14), bg='light yellow')
    quote_label.pack(expand=True)

    if author:
        author_label = tk.Label(window, text=f"- {author}", font=("Courier", 12, "italic"), bg='light blue')
        author_label.pack()

    window.mainloop()




load_dotenv() 

client=OpenAI()

print("Welcome to Daily Inspirational Quote Generator!")


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "you are a quote generator, who finds short, inspirational quotes from famous people based on the type of quote they want. Generate a different quote every time"},
    {"role": "user", "content": "Find a inspirational quote about academic success"}
  ]
)

quote = completion.choices[0].message
print(quote)

# Display the quote in a GUI window
display_quote(quote)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# """
# Created on Tue Dec 26 09:30:15 2023

# @author: kashishsethi
# """



# quotes = [
#     "The best way to predict the future is to invent it. - Alan Kay",
#     "The way to get started is to quit talking and begin doing. - Walt Disney",
#     "Life is what happens when you're busy making other plans. - John Lennon",
#     "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
#     "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats"
# ]

# random_quote= random.choice(quotes)
# print(random_quote)

# # get today's data and format it 
# today_date = datetime.now().strftime("%Y-%m-%d")
# file_name = f"/Users/kashishsethi/anaconda3/python projectsquote-of-the-day-{today_date}.txt"

# # Write the quote to a file 
# with open(file_name, 'w') as file:
#     file.write(random_quote + "\n")
    
# #print("Current working directory:", os.getcwd())
# #print("Current file path:", os.path.abspath(__file__))


# def display_quote():
#     window= tk.Tk()
#     window.title("Daily Inspirational Quote")
#     window.geometry("400x200")
#     window.configure(bg="ivory2")
    
#     quote= random.choice(messages)
#     quote_text, author = quote.split(" - ")
#     quote_label = tk.Label(window, text=quote_text, wraplength=350, justify="center", font=("Modern", 14), bg='DarkSeaGreen1')
#     quote_label.pack(expand=True)

#     author_label = tk.Label(window, text=f"- {author}", font=("Courier", 12, "italic"), bg='DarkSeaGreen3')
#     author_label.pack()

    


#     window.mainloop()
# display_quote()

             
