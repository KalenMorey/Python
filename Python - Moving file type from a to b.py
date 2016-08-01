from tkinter import *
import os
import shutil
import sys
import posixpath

sourcepath = posixpath.join('/Users/kalenmorey/Documents/a')    # Location of Folder a 
destination =  posixpath.join('/Users/kalenmorey/Documents/b')  # Location of Folder b 


# This function locatates all .txt files in folder a and moves them to folder b and prints out their new file path.  
def x ():
    for files in os.listdir('/Users/kalenmorey/Documents/a'):
        src =  posixpath.join(sourcepath,files)
        dst =  posixpath.join(destination,files)
        if files.endswith('.txt'):                 
            print("File: {} ".format(src))
            print("Moved to: {} ".format(dst))
            shutil.move(src,dst)


root = Tk()
root.title("Kalen Enterprises ")
root.configure(background = "RoyalBlue1")
frame1=Frame(root)
frame1.grid()
label1 = Label(frame1, text = "Move all .txt files from folder a to folder b?",
		 fg = "pale goldenrod",
		 bg = "blue4",
		 font = "Helvetica 16 bold italic").pack()

frame2=Frame(root)
frame2.grid()
button1 = Button(frame2, text = "Move Files", command= x).pack()


root.mainloop(  )
root=makeWindow()







