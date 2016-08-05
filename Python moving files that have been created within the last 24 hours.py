from tkinter import *
import os,sys,time
import posixpath
from datetime import datetime,timedelta
import shutil

''' Files created or modified in the past 24 hours are added to folder  "nf"
    and then sent to folder "ho" everyday at 5:00pm '''


def findfiles(source,destination):
    for path,dirs,files in os.walk(source):
        for _file in files:
            if _file.endswith(".txt") :
                src = posixpath.join(source,_file)
                dst = posixpath.join(destination,_file)
                mtime = (os.path.getmtime(src))
                timeDiff = time.time() - mtime
                _24hrsAgo = time.time() - (24 *60 *60)
                last24hrs= time.time() - _24hrsAgo
                if timeDiff < last24hrs:
                    shutil.move(src,dst)
                    print("({}) Moved to: {}".format(_file,dst))
   

def makeWindow():
    source = posixpath.join('/Users/kalenmorey/Documents/nf')
    destination = posixpath.join('/Users/kalenmorey/Documents/ho')

    win = Tk()
    win.title("Kalen Enterprises ")
    win.configure(background = "RoyalBlue1")    
    frame1=Frame(win)
    frame1.grid()
    label1 = Label(frame1, text = "Move files created today",
		 fg = "pale goldenrod",
		 bg = "blue4",
        	 font = "Helvetica 16 bold italic")
    label1.grid(row=0 , column = 1)
    

    frame3=Frame(win)
    frame3.grid()
    button1 = Button(frame3, text = "Move Files", command = lambda:findfiles(source,destination))
    button1.grid(row=2, column=3, sticky = W)
    # Frame for Undo Button
    
    # Undo Button
    button2 = Button(frame3,text = "Undo Move", command = lambda:findfiles(destination,source))
    button2.grid(row=2, column=1, sticky = E)               

win = makeWindow()






                                             

