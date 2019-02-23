#!/usr/bin/env python
# python 3 written in IDLE 3.7.0
# makes a small GUI to use Coinhive URL shortener

# dependencies are tkinter and requests

# API uses secret key so
# should add encryption for saved secret to be on the safe side
# couldn't decide on a module to try, maybe Fernet

# should add function to copy Shortlink to clipboard to skip a UI step


# import tkinter and requests
from tkinter import *
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "https://api.coinhive.com/link/create"
  
# could hardcore your key into json data if you want instead of save/load

# sending post request and saving response as response object 
def send_coinhive_request():
    cnhv_data = {'secret':str(e1.get()), 
        'url':str(e2.get()), 
        'hashes':2048, } 
    r = requests.post(url = API_ENDPOINT, data = cnhv_data) 
  
    # extracting response text and print it to console for console's sake
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
    master.quit()
    master.destroy()

# functions to save/load coinhive key
# should encrypt this shit but whatever for now it works
def save_cnhv_key():
    savedsecret = open('saved.py', 'w')
    savedsecret.write(e1.get())
    savedsecret.close()

def load_cnhv_key():
    loadsecret = open('saved.py', 'r')
    loadedsecret = loadsecret.read()
    e1.delete(0, END)
    e1.insert(END, loadedsecret)
    


# begin GUI


master = Tk()
master.geometry('256x184')
master.grid_columnconfigure(0, weight=1)
Label(master, text="Secret :").grid(row=0, sticky=W)
Label(master, text="URL :").grid(row=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1, sticky=W)
e2.grid(row=1, column=1, sticky=W)

Button(master, text='Shorten', command=send_coinhive_request).grid(row=4, column=1, sticky=EW)
Button(master, text='Quit', command=ragequit).grid(row=5, column=1, sticky=EW)

T = Text(master, height=4)
T.grid(row=3, column=0, sticky=W, columnspan=2)
T.insert(END, "Shortlink will appear here. Saving key makes 2nd file saved.py. Click Load to load saved key.")

Button(master, text='Save Secret', command=save_cnhv_key).grid(row=4, column=0, sticky=EW)
Button(master, text='Load Secret', command=load_cnhv_key).grid(row=5, column=0, sticky=EW)

Label(master, text="hatemail@deathmetal.me").grid(row=6, columnspan=2)

mainloop()

# end gui
