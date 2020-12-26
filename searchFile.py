import os
import PySimpleGUI as sg
import tkinter as tk
from tkinter.messagebox import showinfo

#Create window
root = tk.Tk()
#Specify geometry
root.geometry("320x120")
#Set background color
root.configure(bg="SteelBlue4")
#Set window title
root.title("File Search Application")
#Enter the widgets
l1 = tk.Label(root, text = "Enter the filename to search")
l1.pack()
l1.configure(bg = "Steelblue4", fg = "white")
#Input field for entry of filename
entry1 = tk.Entry(root, width=40)
entry1.pack()

#Function to show popup and location of file
def popup():
    for root, dirs, files in os.walk('C:/Users/pk2/Desktop/'):
        for name in files:
            if (name.split('.')[0]) == str(entry1.get()):
                location = os.path.join(root, name)
    showinfo("Location", location)
        
#Buttons [Search and Close]
b1 = tk.Button(root, text = "Search", command = popup)
b1.pack()
b1.config(width=12)

b2 = tk.Button(root, text = "Close", command=root.destroy)
b2.pack()
b2.config(width=12)

root.mainloop()