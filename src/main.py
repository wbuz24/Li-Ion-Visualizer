
from matplotlib import pyplot as plt
import pandas as pd
import tkinter as tk
import os



def csvread():
    global df
    filePath = entry.get() # grabs filepath from input box
    df = pd.read_excel(filePath)
    z = df['Time']
    x = df['Wh/Kg']
    y = df['Wh/L']

    
    for i in range(28):
       timeEntries[i].delete(0, 'end')
       timeEntries[i].insert(0, [z[i]])


# initialize a window
window = tk.Tk()
window.geometry("1200x800")
window.title("Li-Ion Visualizer")

# initialize an entry box
entry = tk.Entry(window, width = 20)
entry.grid(row = 2, column = 15, padx = (20, 0), pady = 1)
entry.insert(0, os.getcwd() + '/include/Li_ion_battery_figure.xlsx')

timeEntries = []

for i in range(28):
    timeEntries.append(tk.Entry(window, width = 5))
    timeEntries[i].grid(row = i + 5, column = 2, padx = 10, pady = 1)

# create an import button 
import_button = tk.Button(window, text = "Import", command = csvread)
import_button.grid(row = 2, column = 5, padx = (420, 0))

timeLabel = tk.Label(window, text = 'Year')
timeLabel.grid(row = 4, column = 2, padx = 10, pady = 1)


window.mainloop()
