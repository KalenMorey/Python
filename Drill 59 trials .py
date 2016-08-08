from tkinter import *
import os,sys,time
import posixpath
from datetime import datetime,timedelta
import shutil

''' Files created or modified in the past 24 hours are added to folder  "nf"
    and then sent to folder "ho" everyday at 5:00pm '''

class Fileapp:
    def __init__(self,master):
        

        #GUI
        self.master = master
        master.configure(background = "RoyalBlue1")
        self.button1 = Button(master,text = "Choose Source Folder", command = lambda arg:self.get_directory(0)) # Choose Source folder 
        self.button1.grid(row=0, column=1, sticky = N, padx = 10, pady = 10)

        self.button2 = Button(master,text = "Choose Destination Folder", command = lambda arg:self.get_directory(1)) # Choose Destination folder 
        self.button2.grid(row=1, column=1, sticky = N, padx = 10, pady=10) 

        self.button3 = Button(master, text= "Move files", command = lambda arg:findfiles(source,destination)) # Move Files 
        self.button3.grid(row=3,column=1,padx = 10, pady = 10)

        self.button4 = Button(master, text="Undo Move", command=())
        self.button4.grid(row=3,column=2,padx=10,pady=10)
        self.e1=Entry(master,bd=5)
        self.e1.grid(row=0,column=2,sticky = W,padx=5)
        
        self.e2=Entry(master,bd=5)
        self.e2.grid(row=1,column=2,sticky = W,padx =5)

    def get_directory(self,arg): # Choose Source and Directory Folders      
        dir_name = filedialog.askdirectory(parent=self,initialdir='/Users/kalenmorey/Documents')
        if arg ==0:
            self.txtSource.insert(0,dir_name)
        if arg ==1:
            self.txtSource.insert(0,dir_name)
        

        
    '''def findfiles(source,destination): # Move Files 
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
                        print("({}) Moved to: {}".format(_file,dst))'''

    
        
    
        



root = Tk()
App = Fileapp(root)
root.mainloop()







        
    

   

              





