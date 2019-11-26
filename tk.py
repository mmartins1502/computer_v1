


# import gi
# gi.require_version("Gtk", "3.0")
# from gi.repository import Gtk
from computer_v1 import compute

# class App(Gtk.Window):

#     def __init__(self):
#         Gtk.Window.__init__(self, title="Computer v1")
#         self.set_default_size(200, 100)
#         self.set_border_width(10)
#         table = Gtk.Grid()
#         table.set_row_spacing(30)
#         self.add(table)

#         entry = Gtk.Entry()
#         entry.set_text("Entrez votre polynône ici et validez avec \"Entrée\"")
        
#         label = Gtk.Label("")
#         entry.connect("activate", self.cb_activate, label)

#         table.attach(entry, 0, 0, 10, 2)
#         table.attach(label, 0, 1, 10, 10)



#     def cb_activate(self, entry, label):
#         equation = entry.get_text()
#         result = compute(equation)
#         label.set_text(result)

#         return


# win = App()
# win.connect("destroy", Gtk.main_quit)
# win.show_all()
# Gtk.main()



#########################################################################################################################

from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial
from computer_v1 import compute

def update_label(label, stringvar, action):
    if action == 'valider':
        equation = stringvar.get()
        res = compute(equation)
        print(res)
        label.config(text=res)
        stringvar.set('')
    elif action == 'effacer':
        label.config(text='')
        stringvar.set('')


root = Tk()
text = StringVar(root)
label = Label(root, text='')
entry_name = Entry(root, textvariable=text)
button = Button(root, text='Valider', command=partial(update_label, label, text, 'valider'))
clear_button = Button(root, text='Effacer', command=partial(update_label, label, text, 'effacer'))

label.grid(column=0, row=0)
entry_name.grid(column=0, row=1)
button.grid(column=0, row=2)
clear_button.grid(column=0, row=3)

root.mainloop()