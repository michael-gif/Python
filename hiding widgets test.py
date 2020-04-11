# i was trying to hide buttons, but it didn't work. oh well

import tkinter as tk
app = tk.Tk()
app.title("server")
def hidebutton():
    button1.grid_info()
def showbutton():
    button1.grid()
button1 = tk.Button(app,text = "Click to hide", command = hidebutton)
button1.grid(row=0,column=0)
button2 = tk.Button(app,text = "Click to hide", command = showbutton)
button2.grid(row=1,column=0)
tk.mainloop()
