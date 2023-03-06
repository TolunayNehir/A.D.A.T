import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import tkinter as ttk
from tkinter import *
#matplotlib.use('Agg')

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
    elif plotype=="advanced":
        kind=input("Kind:")
        items=input("How many items:")
        array=[]
        while(int(items)>0):
            item=input("item:")
            array.append(str(item))
            items=int(items)-1
        df[array].plot(kind=str(kind))
        plt.grid()
        plt.show()
    input("Press Enter to continue...")

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
    print("Type 1 first 5,2 last 5,3 all variables ,4 filter vairables,5 info")
    type1=input("Type:")
    if type1=="1":
        print(df.head().to_string())
    elif type1=="2":
        print(df.tail().to_string())
    elif type1=="3":
        print(df.to_string())
    elif type1=="4":
        filter1=input("Type filter query:")
        print(df.query(str(filter1)))
    elif type1=="5":
        print(df.info())
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
    plot=input("Do you want plotting:")
    if plot=="yes":
        plottype=input("Plotting type 1 classic,2 customized,3 advanced")
        if plottype=="1":
            plotting(df,"classic")
        elif plottype=="2":
            plotting(df,"customized")
        elif plottype=="3":
            plotting(df,"advanced")
    else:
        print("Analyze finished")
        main()
def csv():
    file=input("Filename:")
    df = pd.read_csv(file)
    print("Data has been dataframed")
    print("Type 1 first 5,2 last 5,3 all variables ,4 filter vairables,5 info")
    type1=input("Type:")
    if type1=="1":
        print(df.head().to_string())
    elif type1=="2":
        print(df.tail().to_string())
    elif type1=="3":
        print(df.to_string())
    elif type1=="4":
        filter1=input("Type filter query:")
        print(df.query(str(filter1)).to_string())
    elif type1=="5":
        print(df.info())
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
        plottype=input("Plotting type 1 classic,2 customized,3 advanced")
        if plottype=="1":
            plotting(df,"classic")
        elif plottype=="2":
            plotting(df,"customized")
        elif plottype=="3":
            plotting(df,"advanced")
    else:
        print("Analyze finished")
        main()


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
