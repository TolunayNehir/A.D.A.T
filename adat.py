import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tkinter as ttk
from tkinter import *
#matplotlib.use('Agg')


def fixdata():
    file=input("filename:")
    type4=input("json or csv:")
    if type4=="csv":
        df = pd.read_csv(file)
    elif type4=="json":
        df=pd.read_json(file)
    else:
        print("Not found")
        main()
    data1=input("Data for type casting:")
    casting=input("1 datetime:")
    if casting=="1":
        df[data1] = pd.to_datetime(df[data1])
        print("Data fixed.")
    else:
        print("Not found")
    
def json():
    file=input("Filename:")
    df = pd.read_json(file)
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ,4 filter vairables")
    type1=input("Type:")
    if type1==1:
        print(df.head())
    elif type1==2:
        print(df.tail())
    elif type1==3:
        print(df)
    elif type1==4:
        filter1=input("Type filter query:")
        print(df[str(filter1)])
    else:
        print("Not Found")
    operation=input("Do you want replace emty cells:")
    if operation=="yes":
        type3=input("1 Spesific column,2 all cells")
        if type3=="1":
            column=input("Data column:")
            value=input("Value for fill:")
            df[str(column)].fillna(value, inplace = True)
        elif type3=="2":
            value=input("Value for fill:")
            df.fillna(value, inplace = True)
        else:
            print("Not found")
    plot=input("Do you want plotting")
    if plot=="yes":
        plotype=input("Plotting type 1 classic,2 customized")
        if plottype=="classic":
            plotting(df,"classic")
        elif plottype=="cutomized":
            plotting(df,"customized")
    else:
        print("Analyze finished")
        main()
def csv():
    file=input("Filename:")
    df = pd.read_csv(file)
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ,4 filter vairables")
    type1=input("Type:")
    if type1==1:
        print(df.head())
    elif type1==2:
        print(df.tail())
    elif type1==3:
        print(df)
    elif type1==4:
        filter1=input("Type filter query:")
        print(df[str(filter1)])
    else:
        print("Not Found")
    operation=input("Do you want replace emty cells:")
    if operation=="yes":
        type3=input("1 Spesific column,2 all cells")
        if type3=="1":
            column=input("Data column:")
            value=input("Value for fill:")
            df[str(column)].fillna(value, inplace = True)
        elif type3=="2":
            value=input("Value for fill:")
            df.fillna(value, inplace = True)
        else:
            print("Not found")
    plot=input("Do you want plotting")
    if plot=="yes":
        plotype=input("Plotting type 1 classic,2 customized")
        if plottype=="classic":
            plotting(df,"classic")
        elif plottype=="cutomized":
            plotting(df,"customized")
    else:
        print("Analyze finished")
        main()

def plotting(df,plotype):
    if plotype=="classic":
        print("plotting started:")
        df.plot()
        plt.grid()
        plt.show()
    elif plotype=="customized":
        x=input("X:")
        y=input("Y:")
        kind=input("Kind:")
        print("plotting started:")
        df.plot(kind=str(kind),x=str(x),y=str(y))
        plt.grid()
        plt.show()

def main():
    print("File Type: 1 csv,2 json,Operations: 3 fix data")
    filetype=input("File Type:")
    if filetype=="1":
        csv()
    elif filetype=="2":
        json()
    elif filetype=="3":
        fixdata()
    else:
        print("Not found")

main()


