#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#Python 3.5.0

import tkinter as tk
from tkinter import *
import os,sys,time
import posixpath
from datetime import datetime,timedelta
import shutil
import sqlite3


        

class Fileapp(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #GUI
        
        self.master = master
        master.configure(background = "GhostWhite")

        # Labels

        self.label2 = Label(master,text = "Select Source Folder")
        self.label2.grid(row=3, column=1, sticky=W)

        self.label3 = Label(master, text ="Select Destination Folder")
        self.label3.grid(row=4, column=1, sticky=W)

        #Buttons
        
        self.button1 = Button(master,text = "Browse", command = lambda: self.get_directory(0)) # Choose Source folder 
        self.button1.grid(row=3, column=3, sticky = E, padx = 10, pady = 10)

        self.button2 = Button(master,text = "Browse", command = lambda: self.get_directory(1)) # Choose Destination folder 
        self.button2.grid(row=4, column=3, sticky = N, padx = 10, pady=10) 

        self.button3 = Button(master, text= "Move files", command = lambda: self.findfiles(3)) # Move Files 
        self.button3.grid(row=5,column=2,padx = 10, pady = 10, sticky=W)

        self.button4 = Button(master, text= "Undo",command = lambda: self.findfiles(4)) # Move Files 
        self.button4.grid(row=5,column=3,padx = 10, pady = 10, sticky=W)

        self.button5 = Label(master, text = 'Last file transfered at')
        self.button5.grid(row=0, column=1, pady = 20)


        self.txttime=Entry(master,bd=5)
        self.txttime.grid(row=0,column =2,sticky=W+E,padx=5)

        self.txtSource = Entry(master,bd=5)
        self.txtSource.grid(row=3,column=2,sticky = W,padx=5)
        
        self.txtDestination = Entry(master,bd=5)
        self.txtDestination.grid(row=4,column=2,sticky = W,padx =5)

        self.db()

        self.last_file_move()

    def db(self):
        conn = sqlite3.connect('FileCheck.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS file_time(ID INTEGER PRIMARY KEY AUTOINCREMENT, datestamp TEXT)") 
        conn.commit()
        conn.close()



    def last_file_move(self):        
            conn = sqlite3.connect('FileCheck.db')
            c = conn.cursor()
            sql = ("Select * FROM file_time WHERE ID=(SELECT MAX(ID) FROM file_time)")
            for row in c.execute(sql):
                self.txttime.insert(0,row)
                

    # Take the last file check and display it in the entry field 
            

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
      
        if arg == 3:

            source = self.txtSource.get()
            destination = self.txtDestination.get()
            print("source: {}".format(source))
            print("destination: {}".format(destination))
            
            conn = sqlite3.connect('FileCheck.db')
            c = conn.cursor()
   
            for files in os.listdir(source):
                file_names=files
                if files.endswith(".txt") :
                    src = posixpath.join(source,files)
                    dst = posixpath.join(destination,files)
                    mtime = (os.path.getmtime(src))
                    timeDiff = time.time() - mtime
                    _24hrsAgo = time.time() - (24 *60 *60)
                    last24hrs= time.time() - _24hrsAgo
                    if timeDiff < last24hrs:
                        shutil.move(src,dst)
                        now=time.time()
                        import datetime
                        date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
                        print("({}) Moved to: {}".format(files,dst))
                        print("({}) File checked at: {}".format(files,date))

                        #Inserting values into table 'newfiles'

                        c.execute("INSERT INTO file_time (datestamp) VALUES(?)",(date,))
                        conn.commit()

                                                                     

        if arg == 4:
            source = self.txtSource.get()
            destination = self.txtDestination.get()
            print("source: {}".format(source))
            print("destination: {}".format(destination))
            for files in os.listdir(destination):
                if files.endswith(".txt") :
                    src = posixpath.join(source,files)
                    dst = posixpath.join(destination,files)
                    mtime = (os.path.getmtime(dst))
                    timeDiff = time.time() - mtime
                    _24hrsAgo = time.time() - (24 *60 *60)
                    last24hrs= time.time() - _24hrsAgo
                    if timeDiff < last24hrs:
                        shutil.move(dst,src)
                        print("({}) Moved to: {}".format(files,dst))

        
                
                
      
root = Tk()
root.title('Daily File Transfer')
App = Fileapp(root)
root.mainloop()








        
    

   

              





