import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import tkinter as tk
from mplcursors import cursor
import mplcursors
import os

def csvread():
    global df, tt
    filePath = entry.get()       # grabs filepath from input box
    df = pd.read_excel(filePath) # stores data in a dataframe
    tt = df["Year"].values
    
    graphButton.grid(row = 4, column = 15, pady = 1) 

def ragoneGraph(): # 
    fig = plt.figure(figsize = (10, 7))
    ax = plt.subplot(projection='3d')
    A = ax.scatter(df.loc[0:4,"Wh/kg"], df.loc[0:4,"Year"], df.loc[0:4,"W/kg"], color = "blue", marker = ".", depthshade = False)
    #print(hex(id(A)))
    B = ax.scatter(df.loc[5:33,"Wh/kg"], df.loc[5:33,"Year"], df.loc[5:33,"W/kg"], color = "red", marker = ".", depthshade = False)
    C = ax.scatter(df.loc[34:42,"Wh/kg"], df.loc[34:42,"Year"], df.loc[34:42,"W/kg"], color = "black", marker = ".", depthshade = False)
    D = ax.scatter(df.loc[43:65,"Wh/kg"], df.loc[43:65,"Year"], df.loc[43:65,"W/kg"], color = "green", marker = ".", depthshade = False)
    E = ax.scatter(df.loc[66,"Wh/kg"], df.loc[66,"Year"], df.loc[66,"W/kg"], color = "orange", marker = "*", depthshade = False, s = 40)

    plt.title("Evolution of Li-ion Energy and Power Density", fontweight='bold')
    ax.set_xlabel('Energy Density (Wh/kg)', fontweight='bold')
    ax.set_ylabel('Year', fontweight='bold')
    ax.set_zlabel('Power Density (W/kg)', fontweight='bold')

    plt.locator_params(axis="both", integer=True, tight=True)
    
    cursor = mplcursors.cursor(hover=True)
    @cursor.connect("add")
    def on_add(sel):
        if hex(id(A)) == str(sel.artist)[55:][:-1]:
            sel.annotation.set(text=str(df.loc[sel.index, "Year"]) + ", " + str(df.loc[sel.index, "W/kg"]) + " W/kg, " + str(df.loc[sel.index, "Wh/kg"]) + " Wh/kg" + "\n" + str(df.loc[sel.index, "Reference"]))
        if hex(id(B)) == str(sel.artist)[55:][:-1]:
            sel.annotation.set(text=str(df.loc[sel.index + 5, "Year"]) + ", " + str(df.loc[sel.index + 5, "W/kg"]) + " W/kg, " + str(df.loc[sel.index + 5, "Wh/kg"]) + " Wh/kg" + "\n" + str(df.loc[sel.index, "Reference"]))
        if hex(id(C)) == str(sel.artist)[55:][:-1]:
            sel.annotation.set(text=str(df.loc[sel.index + 34, "Year"]) + ", " + str(df.loc[sel.index + 34, "W/kg"]) + " W/kg, " + str(df.loc[sel.index + 34, "Wh/kg"]) + " Wh/kg" + "\n" + str(df.loc[sel.index, "Reference"]))
        if hex(id(D)) == str(sel.artist)[55:][:-1]:
            sel.annotation.set(text=str(df.loc[sel.index + 42, "Year"]) + ", " + str(df.loc[sel.index + 42, "W/kg"]) + " W/kg, " + str(df.loc[sel.index + 42, "Wh/kg"]) + " Wh/kg" + "\n" + str(df.loc[sel.index, "Reference"]))
        
    plt.show()

# initialize a window
window = tk.Tk()
window.geometry("500x500")
window.title("Li-Ion Visualizer")

# initialize an entry box
entry = tk.Entry(window, width = 20)
entry.grid(row = 2, column = 15, padx = (20, 0), pady = (220, 0))
entry.insert(0, '../Li-Ion-Visualizer/include/Li_ion_battery_figure.xlsx')

# create an import button 
import_button = tk.Button(window, text = "Import", command = csvread)
import_button.grid(row = 2, column = 5, padx = (170, 0), pady = (220, 0))

graphButton = tk.Button(window, width = 5, text = "Graph", command = ragoneGraph)

window.mainloop()
