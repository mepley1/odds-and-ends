#!/usr/bin/env python
# python 3 written in IDLE 3.7.0
# makes a small GUI to use Coinhive URL shortener API

# dependencies are tkinter and requests

# API uses secret key so
# should add encryption for saved secret to be on the safe side
# couldn't decide on a module to try, maybe fernet or hashlib

# should add function to copy Shortlink to clipboard to skip a UI step

####################################

# import tkinter and requests
from tkinter import *
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "https://api.coinhive.com/link/create"
  
# could hardcode your key into json data if you want instead of save/load

# sending post request and saving response as response object 
def send_coinhive_request():
    cnhv_data = {'secret':str(e1.get()), 
        'url':str(e2.get()), 
        'hashes':str(e3.get()), } 
    r = requests.post(url = API_ENDPOINT, data = cnhv_data) 
  
    # extract response text and print it to console for console's sake
    cnhv_url = r.text
    print("The response is:%s"%cnhv_url)

    # remove extra backslashes from URL
    line = cnhv_url
    for badslash in '\\':  
        line = line.replace(badslash,'')
    print ('Formatted Shortlink:')
    print (line)
    # update result box in GUI
    T.delete("1.0", END)
    T.insert(END, str(line))

# quit
def ragequit():
    print("quitting..")
    master.quit()
    master.destroy()

# functions to save/load coinhive key
# should encrypt this shit but whatever for now it works
def save_cnhv_key():
    savedsecret = open('savegame.py', 'w')
    savedsecret.write(e1.get())
    savedsecret.close()

def load_cnhv_key():
    loadsecret = open('savegame.py', 'r')
    loadedsecret = loadsecret.read()
    e1.delete(0, END)
    e1.insert(END, loadedsecret)
    loadedsecret.close()




print('making GUI...')
print('If you get error about SSL here when you try to shorten, wait a while and try again.')

# begin GUI
master = Tk()
master.geometry('256x218')
master.grid_columnconfigure(0, weight=1)
master.grid_columnconfigure(1, weight=1)
master.title('Coinhive URL Shortener')
Label(master, text="Secret :").grid(row=0, sticky=W)
Label(master, text="URL :").grid(row=1, sticky=W)
Label(master, text="Hashes :").grid(row=2, sticky=W)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1, sticky=EW)
e2.grid(row=1, column=1, sticky=EW)
e2.insert(END, "https://")
e3.grid(row=2, column=1, sticky=EW)
e3.insert(END, "1024")

Button(master, text='S H O R T E N', command=send_coinhive_request, activebackground="#00ff00").grid(row=5, column=1, sticky=EW)
Button(master, text='Quit', command=ragequit).grid(row=6, column=1, sticky=EW)

T = Text(master, height=5)
T.grid(row=4, column=0, sticky=W, columnspan=2)
T.insert(END, "Shortlink will appear here. Saving key makes 2nd file savegame.py. Click Load to load saved key. If SSL error in console wait a while.")

Button(master, text='Save Key', command=save_cnhv_key).grid(row=5, column=0, sticky=EW)
Button(master, text='Load Key', command=load_cnhv_key).grid(row=6, column=0, sticky=EW)

Label(master, text="hatemail@deathmetal.me", background="black", fg="green").grid(row=7, columnspan=2, sticky=EW)

mainloop()

# end gui
