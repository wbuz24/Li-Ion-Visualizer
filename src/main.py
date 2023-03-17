import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import tkinter as tk
import os



def csvread():
    global df, x, y, z
    filePath = entry.get() # grabs filepath from input box
    df = pd.read_excel(filePath)
    z = df['Year']
    x = df['Wh/kg']
    y = df['W/kg']
    for i in range(df.shape[0]):
        if (i > 0 and z[i - 1] != z[i]):
            curr_year = tk.Label(window, text = z[i])
            curr_year.grid(row = i + 5, column = 2, padx = 2, pady = 1)
    #    curr_power = tk.Label(window, text = x[i])
    #    curr_power.grid(row = i + 5, column = 3, padx = 10, pady = 1)
    #    curr_energy = tk.Label(window, text = y[i])
    #    curr_energy.grid(row = i + 5, column = 4, padx = 10, pady = 1)

    graphButton.grid(row = 20, column = 15, pady = 1)
def ragoneGraph():
    ax = plt.figure().gca(projection='3d')
    ax.scatter(z, x, y)
    plt.show()

# initialize a window
window = tk.Tk()
window.geometry("1200x800")
window.title("Li-Ion Visualizer")

# initialize an entry box
entry = tk.Entry(window, width = 20)
entry.grid(row = 2, column = 15, padx = (20, 0), pady = 1)
entry.insert(0, os.getcwd() + '/include/Li_ion_battery_figure.xlsx')

# create an import button 
import_button = tk.Button(window, text = "Import", command = csvread)
import_button.grid(row = 2, column = 5, padx = (370, 0))

timeLabel = tk.Label(window, text = 'Year')
timeLabel.grid(row = 4, column = 2, padx = 10, pady = 1)

#powerLabel = tk.Label(window, text = 'Wh/kg')
#powerLabel.grid(row = 4, column = 3, padx = 2)

#energyLabel = tk.Label(window, text = 'W/kg')
#energyLabel.grid(row = 4, column = 4, padx = 2)

graphButton = tk.Button(window, width = 5, text = "Graph", command = ragoneGraph)

window.mainloop()
