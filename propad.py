from tkinter import Tk,scrolledtext,filedialog,END,messagebox
from tkinter import *
import tkinter.scrolledtext as ScrolledText
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfile,asksaveasfilename
import datetime as dt
import tkinter.scrolledtext as st
import os
from tkinter import ttk,colorchooser
root= Tk()
root.geometry("800x1000")
root.title("Propad v1.0")
root.wm_iconbitmap("i.ico")
TextArea=scrolledtext.ScrolledText(root,font="Cooper 40",bg="#151B54",fg="#ff00ff",cursor="spider")
TextArea.pack()

def help1():
    tmsg.showinfo("Help","Sorry!This Service will available on v2.0 ")
def rate():
       value=tmsg.askquestion("Propad rate","Do you like to work on it?")
       if value == "yes":
           msg1="***Thank you for supporting us ***"
           tmsg.showinfo("Propad",msg1)
       else:
               msg2="Share your problem about this app in our gmail"
               tmsg.showinfo("Propad",msg2)   
def myfunc():
            pass
def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - propad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()



def savefile():
    global file
    if file == None:
        file =asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:

            root.title(os.path.basename(file) + " - Propad")
            file= open(file, "w")
            file.write(TextArea.get(1.0, END))
            file.close()
            
            
    else:

        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def exit():
    if messagebox.askyesno("Exit","Do you want to Exit Propad?"):
        root.destroy()
def newfile():
    global file
    root.title("United -Propad")
    file= None
    
    if len(TextArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesnocancel("Save","Do you want to Save"):
            savefile()
        else:
            root.destroy()
            
def cut(event):
    TextArea.event_generate(("<<Cut>>"))
def copy(event):
    TextArea.event_generate(("<<Copy>>"))
def paste(event):
    TextArea.event_generate(("<<Paste>>"))
def date():
    root=Tk()
    root.title("Date&Time")
    root.configure(bg="black")
    root.wm_iconbitmap("i.ico")
    date = dt.datetime.now()
    time=dt.datetime.now()
    format_date = f"{date:%a, %b %d %Y}"
    format_time= f"{time:%H:%M:%S}"
    w = Label(root,text=format_date, fg="white", bg="black", font=("helvetica", 40))
    w.pack()
    x= Label(root,text=format_time, fg="white", bg="black", font=("monster", 40))
    x.pack()
def window():
    tmsg.showinfo('Background',"This feature is available on next version.<<<Thank for suscribe>>>")
   
def window1():
    tmsg.showinfo('TextColor',"This feature is available on next version.<<<Thank for suscribe>>>")
def window2():
    tmsg.showinfo('TextSize',"This feature is available on next version.<<<Thank for suscribe>>>")
def window3():
    tmsg.showinfo('TextStyle',"This feature is available on next version.<<<Thank for suscribe>>>")
def window4():
    tmsg.showinfo('Photo/Image',"This feature is available on next version.<<<Thank for suscribe>>>")
def window5():
    import thikaipaint
   
                   
#def check():
    #new_window=Toplevel(root)
    #new_window.title("Background with Lucky Color Mode")
    #new_window.geometry("500x1000")
    #new_window.wm_iconbitmap("i.ico")
    #m9=Button(new_window,text="1. Black&Green",bg="black",fg="green",padx=50,pady=20,command=window)
    #m9.place(x=0,y=1)
    #m9=Button(new_window,text= "2. Luckypoint&RED ",bg="#151B54",fg="red",padx=50,pady=20,command=window)
    #m9.place(x=0,y=100)
    #m9=Button(new_window,text= "3. Luckypoint&Green ",bg="#151B54",fg="green",padx=50,pady=20,command=window)
    #m9.place(x=0,y=200)
    #m9=Button(new_window,text= "4. Luckypoint&Magenta ",bg="#151B54",fg="#ff00ff",padx=50,pady=20,command=window)
    #m9.place(x=0,y=300)
    #m9=Button(new_window,text= "5. Luckypoint&White ",bg="#151B54",fg="white",padx=50,pady=20,command=window)
    #m9.place(x=0,y=400)
    #m9=Button(new_window,text= "6. Luckypoint&Orange ",bg="#151B54",fg="#FF8C00",padx=50,pady=20,command=window)
    #m9.place(x=0,y=500)
    


    
#file start
mainmenu=Menu(root)
m1=Menu(mainmenu)
m1.add_command(label="New         CTRL+N",command=newfile)
m1.add_command(label="Open        CTRL+O",command=openFile)
m1.add_command(label="Save        CTRL+S",command=savefile)
m1.add_command(label="Save as",command=savefile)
m1.add_separator()
m1.add_command(label="Exit     ALT+F4",command=exit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

#edit
m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut      CTRL+X",command=cut)
m2.add_command(label="Copy     CTRL+C",command=copy)
m2.add_command(label="Paste    CTRL+V",command=paste)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)
#page setup
m0=Menu(mainmenu,tearoff=0)
m0.add_command(label="Background",command=window)
m0.add_command(label="Text color",command=window1)
m0.add_command(label="Text size",command=window2)
m0.add_command(label="Text style",command=window3)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Page setup",menu=m0)
#insert
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Photo/Image",command=window4)
m3.add_command(label="Paint ",command=window5)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Insert",menu=m3)
#internet
m4=Menu(mainmenu,tearoff=0)
m4.add_command(label="Language Transfer",command=myfunc)
m4.add_command(label="Dictionary",command=myfunc)
m4.add_command(label="Website",command=myfunc)
m4.add_command(label="Wikipedia",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Internet",menu=m4)
#rate us
m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help1)
m3.add_command(label="Rate us",command=rate)
mainmenu.add_cascade(label="About Us",menu=m3)
root.config(menu=mainmenu)
m5=Menu(mainmenu,tearoff=0)
m5.add_command(label="Date&Time",command=date)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Date&Time",menu=m5)
root.mainloop()





