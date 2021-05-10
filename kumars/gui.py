import tkinter
from tkinter import *
import tkinter as tk
from mct import morse
from PIL import ImageTk


def copy_text():
  message = inputter.get()
  x=morse(message)
  text = x
  clip = Tk()
  clip.withdraw()
  clip.clipboard_clear()
  clip.clipboard_append(text)
  clip.destroy()
  


def display():
  message = inputter.get()
  x=morse(message)
  notes = Label(window, text=x, font="times 15")
  notes.place(x=10, y=30) 
  notes.after(3000,notes.destroy)



window = Tk()
window.geometry("350x350")  
window.iconbitmap('favicon.ico')
#bg=PhotoImage(file="bkg.png") 
#bg_label=Label(window,image=bg) 
#bg_label.place(x=0,y=0,relwidth=1,relheight=1)


window.title("Morse code translator")


inputt_heading = Label(window, text="INPUT TEXT HERE", font="laoui")
inputt_heading.place(x=10, y=70)

inputter = Entry(window, width=30)
inputter.place(x=110, y=100)

image1 = tk.PhotoImage(file="copy.png")  
image1 = image1.subsample(19,19)

copy_to_clipboard = Button(
    window, text="copy to clipboard",image=image1, command=copy_text, font="times4",borderwidth=0)
copy_to_clipboard.place(x=190, y=130)

#image2 = tk.PhotoImage(file="translator.png")  
#image2 = image2.subsample(19,19)
printa = Button(window, text="convert",command=display, font="arial",borderwidth=0)
printa.place(x=10, y=130)






window.mainloop()