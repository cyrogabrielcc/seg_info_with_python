from tkinter import *
import webbrowser

root = Tk( )

root.title('Open Browser')
root.geometry('300x200')

def google():
    webbrowser.open('https://www.google.com')

mygoogle = Button(root, text="open Chrome", command=google).pack(pady=20)
root.mainloop()











