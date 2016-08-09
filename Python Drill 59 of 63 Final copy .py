#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#Python 3.5.0

import tkinter as tk
from tkinter import *
import os,sys,time
import posixpath
from datetime import datetime,timedelta
import shutil

''' Files created or modified in the past 24 hours are added to folder  "nf"
    and then sent to folder "ho" everyday at 5:00pm '''

class Fileapp(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #GUI
        self.master = master
        master.configure(background = "RoyalBlue1")
        self.button1 = Button(master,text = "Choose Source Folder", command = lambda: self.get_directory(0)) # Choose Source folder 
        self.button1.grid(row=0, column=1, sticky = NW, padx = 10, pady = 10)

        self.button2 = Button(master,text = "Choose Destination Folder", command = lambda: self.get_directory(1)) # Choose Destination folder 
        self.button2.grid(row=1, column=1, sticky = N, padx = 10, pady=10) 

        self.button3 = Button(master, text= "Move files", command = lambda: self.findfiles(3)) # Move Files 
        self.button3.grid(row=3,column=1,padx = 10, pady = 10, sticky=W)

        self.button4 = Button(master, text= "Undo", command = lambda: self.findfiles(4)) # Move Files 
        self.button4.grid(row=3,column=3,padx = 10, pady = 10, sticky=W)

        self.txtSource = Entry(master,bd=5)
        self.txtSource.grid(row=0,column=2,sticky = W,padx=5)
        
        self.txtDestination = Entry(master,bd=5)
        self.txtDestination.grid(row=1,column=2,sticky = W,padx =5)

    def get_directory(self,arg): # Choose Source and Directory Folders
        print("arg: {}".format(arg))
        dir_name = filedialog.askdirectory(parent=self,initialdir='/Users/kalenmorey/Documents')
        if arg == 0:
            self.txtSource.delete(0, END) # clear textbox
            self.txtSource.insert(0, dir_name) # add new data in text box
        elif arg == 1:
            self.txtDestination.delete(0, END)
            self.txtDestination.insert(0, dir_name)
        
    def findfiles(self,arg): # Move Files
        source = self.txtSource.get()
        destination = self.txtDestination.get()
        print("source: {}".format(source))
        print("destination: {}".format(destination))
        if arg == 3:
            
            for files in os.listdir(source):
                if files.endswith(".txt") :
                    src = posixpath.join(source,files)
                    dst = posixpath.join(destination,files)
                    mtime = (os.path.getmtime(src))
                    print (mtime)
                    timeDiff = time.time() - mtime
                    _24hrsAgo = time.time() - (24 *60 *60)
                    last24hrs= time.time() - _24hrsAgo
                    if timeDiff < last24hrs:
                        shutil.move(src,dst)
                        print("({}) Moved to: {}".format(files,dst))

        if arg == 4:
 
            for files in os.listdir(destination):
                if files.endswith(".txt") :
                    src = posixpath.join(source,files)
                    dst = posixpath.join(destination,files)
                    mtime = (os.path.getmtime(dst))
                    print (mtime)
                    timeDiff = time.time() - mtime
                    _24hrsAgo = time.time() - (24 *60 *60)
                    last24hrs= time.time() - _24hrsAgo
                    if timeDiff < last24hrs:
                        shutil.move(dst,src)
                        print("({}) Moved to: {}".format(files,dst))

        
root = Tk()
App = Fileapp(root)
root.mainloop()







        
    

   

              





