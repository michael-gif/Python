# i was trying out the treeview widget from tkinter

import tkinter as tk
import tkinter.ttk as ttk
app = tk.Tk()
app.title("treeview test")
app.geometry('350x250')
treeview = ttk.Treeview(app)
treeview.insert('','0','clients',text='Clients')
treeview.insert('clients','end','user1',text='user1')
treeview.insert('clients','end','user2',text='user2')
treeview.insert('clients','end','user3',text='user3')
treeview.insert('clients','end','user4',text='user4')
treeview.insert('','end','logs',text = 'Logs')
treeview.heading('#0',text='Files')
treeview.place(x=0,y=0)
tk.Label(app,text = 'Contents').place(x=225,y=0)
labelvalue = tk.StringVar(app)
label1 = tk.Label(app,textvariable = labelvalue,bg='white').place(x=205,y=25,width=100,height=200)
tk.mainloop()
