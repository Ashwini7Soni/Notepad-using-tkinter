from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import colorchooser
import os



def newFile(event=None):
    global file
    root.title("Untitled-Notepad")
    file = NONE
    Textarea.delete(1.0, END)

def openFile(event=None):
    global file
    file = askopenfilename(defaultextension = ".txt",
                       filetypes = [("All Files","*.*"),
                                    ("Text Documents","*.txt")])
    if file == "":
        file = NONE
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Textarea.delete(1.0, END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())
        f.close()


def saveFile(event=None):
    global file
    if file == NONE:
        file = asksaveasfilename(initialfile = "untitled.txt",
                                 defaultextension = ".txt",
                       filetypes = [("All Files","*.*"),
                                    ("Text Documents","*.txt") ] )
        if file == "":
            file = NONE
        else:
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        #open existing file, edit and then save
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()

def saveasFile():
    global file
    if file != NONE :
        file = asksaveasfilename(initialfile="untitled.txt",
                                 defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = NONE
        else:
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")



def quitApp():
    root.destroy()

def cut(event=None):
    Textarea.event_generate(("<<Cut>>"))

def copy(event=None):
    Textarea.event_generate(("<<Copy>>"))

def paste(event=None):
    Textarea.event_generate(("<<Paste>>"))

def undo(event=None):
    Textarea.event_generate(("<<Undo>>"))

def redo(event=None):
    Textarea.event_generate(("<<Redo>>"))



def selectAll(event=None):
    Textarea.tag_add('sel', '1.0', 'end')
    return "break"

def deleteAll(event=None):
    Textarea.delete(1.0,END)

def about():
    showinfo("Notepad", "RELEASE NOTES \n \n Version: RAS 1.0 \n\n Developed by :\n \n Ashwini Soni\n Radhika Bharani"
                        " \n Sunita Dodve  ")




def setFont():
    fontObj=Tk()
    fontObj.title("Font")
    fontObj.geometry("430x300")
    Label(fontObj, text="Font: ", font="14").grid(row=0, sticky=E, pady=5)
    font1= StringVar(fontObj)
    font1.set("Consolas")
    Option= OptionMenu(fontObj,font1,"Consolas", "Constantia",
                       "Cooper", "Copperplate Gothic",
                       "Elephant", "Fixedsys","Edwardian Script ITC")
    Option.grid(row=0, column=1, sticky= W, padx=15, pady=5)

    Label(fontObj, text="Font Style: ", font="14").grid(row=1, sticky=E, pady=5)
    fontStyle= StringVar(fontObj)
    fontStyle.set("Regular")
    Option2 = OptionMenu(fontObj, fontStyle, "Regular", "Italic",
                        "Bold")
    Option2.grid(row=1, column=1, sticky= W, padx=15, pady=5)

    Label(fontObj, text="Size: ", font="14").grid(row=2, sticky= E, pady=5)
    fontSize= IntVar(fontObj)
    fontSize.set("11")
    Option3 = OptionMenu(fontObj, fontSize, "11", "12",
                         "14", "16", "18", "20","22","24","26","28","36",
                         "48", "60", "72")
    Option3.grid(row=2, column=1, sticky= W, padx=15, pady=5)

    Label(fontObj, text="Font Colour: ", font="14").grid(row=3, sticky=E, pady=5)

    def selectColour():
        color1 = colorchooser.askcolor()[1]
        t=Textarea.selection_get()
        Textarea.tag_add(t, 1.0, END)
        Textarea.tag_config(t, foreground=color1)

    Button(fontObj, text="Choose colour", command= selectColour).grid(row=3, column=1, sticky= W, padx=15, pady=5)


    def actualfontSetting():
        a = font1.get()
        b = fontSize.get()
        c = fontStyle.get()

        myFont = Font(family=a, weight="normal", size=b)

        if c== "Bold":
            myFont=Font(family=a, weight="bold", size=b)
        if c== "Regular":
            myFont = Font(family=a, weight="normal", size=b)
        if c == "Italic":
            myFont = Font(family=a, slant="italic", size=b)

        Textarea.configure(font=myFont)
        fontObj.destroy()

    def cancel():
        fontObj.destroy()




    Button(fontObj,text="OK", command= actualfontSetting).grid(row=4,
                                                               column=1,
                                                               sticky= W,
                                                               pady=5)

    Button(fontObj, text="Cancel", command=cancel).grid(row=4,
                                                        column=2,
                                                        sticky= E,
                                                        pady=5)







if __name__ == '__main__':
    root = Tk()

    root.title("Untitled - Notepad")
    root.iconbitmap(r'notepad.ico')
    root.geometry("1030x490")

    #Canvas to add another Menu Bar of icons



    canvas= Canvas(root, width=1030, height= 32)
    canvas.pack(fill= X)

    file = NONE

    image1 = Image.open("new.png")
    new = ImageTk.PhotoImage(image1)
    label1=Label(canvas, image= new)
    label1.pack(side=LEFT)
    label1.bind('<Button-1>', newFile)

    image2 = Image.open("open.png")
    openImage = ImageTk.PhotoImage(image2)
    label2=Label(canvas, image=openImage)
    label2.pack(side=LEFT)
    label2.bind('<Button-1>', openFile)

    image3 = Image.open("save.png")
    save = ImageTk.PhotoImage(image3)
    label3=Label(canvas, image=save)
    label3.pack(side=LEFT)
    label3.bind('<Button-1>', saveFile)

    image4 = Image.open("cut.png")
    cutImg = ImageTk.PhotoImage(image4)
    label4=Label(canvas, image=cutImg)
    label4.pack(side=LEFT)
    label4.bind('<Button-1>', cut)

    image5 = Image.open("copy.png")
    copyImg = ImageTk.PhotoImage(image5)
    label5=Label(canvas, image=copyImg)
    label5.pack(side=LEFT)
    label5.bind('<Button-1>', copy)

    image6 = Image.open("paste.jpg")
    pasteImg = ImageTk.PhotoImage(image6)
    label6=Label(canvas, image=pasteImg)
    label6.pack(side=LEFT)
    label6.bind('<Button-1>', paste)

    image7 = Image.open("undo.png")
    undoImg = ImageTk.PhotoImage(image7)
    label7=Label(canvas, image=undoImg)
    label7.pack(side=LEFT)
    label7.bind('<Button-1>', undo)

    image8 = Image.open("redo.png")
    redoImg = ImageTk.PhotoImage(image8)
    label8=Label(canvas, image=redoImg)
    label8.pack(side=LEFT)
    label8.bind('<Button-1>', redo)

    #Add Textarea
    Textarea = Text(root, font = "lucida 14",undo=TRUE)
    Textarea.pack(expand = TRUE, fill = BOTH)



    #add menu
    MenuBar = Menu(root)
    FileMenu = Menu(MenuBar, tearoff = 0)

    #add File command
    FileMenu.add_command(label="New", accelerator='Ctrl+N', command=newFile)
    Textarea.bind('<Control-N>', newFile)
    Textarea.bind('<Control-n>', newFile)
    FileMenu.add_command(label="Open...",accelerator='Ctrl+O', command=openFile)
    Textarea.bind('<Control-O>', openFile)
    Textarea.bind('<Control-o>', openFile)
    FileMenu.add_command(label="Save",accelerator='Ctrl+S', command=saveFile)
    Textarea.bind('<Control-S>', saveFile)
    Textarea.bind('<Control-s>', saveFile)
    FileMenu.add_command(label="Save As...",command=saveasFile)


    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label = "File", menu = FileMenu)


    #edit
    EditMenu = Menu(MenuBar, tearoff = 0)
    EditMenu.add_command(label = "Cut",accelerator="ctrl+X", command = cut)

    Textarea.bind('<Control-X>', cut)
    Textarea.bind('<Control-x>', cut)
    EditMenu.add_command(label="Copy",accelerator="ctrl+C", command = copy)
    Textarea.bind('<Control-X>', copy)
    Textarea.bind('<Control-x>', copy)
    EditMenu.add_command(label="Paste",accelerator="ctrl+V", command = paste)
    Textarea.bind('<Control-X>', paste)
    Textarea.bind('<Control-x>', paste)

    EditMenu.add_separator()

    EditMenu.add_command(label="Undo",accelerator="ctrl+Z", command=undo)
    Textarea.bind('<Control-X>', undo)
    Textarea.bind('<Control-x>', undo)
    EditMenu.add_command(label="Redo", command=redo)
    EditMenu.add_command(label="Select All",accelerator="ctrl+A",
                         command=selectAll)
    Textarea.bind('<Control-A>', selectAll)
    Textarea.bind('<Control-a>', selectAll)

    EditMenu.add_separator()

    EditMenu.add_command(label="Delete",
                         command=deleteAll)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    root.config(menu=MenuBar)

    #format
    FormatMenu = Menu(MenuBar, tearoff=0)
    FormatMenu.add_command(label="Font...", command=setFont)
    MenuBar.add_cascade(label="Format", menu=FormatMenu)



    #help
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)

    MenuBar.add_cascade(label = "Help", menu = HelpMenu)

    #scrollbar
    scrollbar = Scrollbar(Textarea)
    scrollbar.pack(side=RIGHT, fill=Y)

    scrollbar.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scrollbar.set)




    root.mainloop()

