#!/usr/bin/env python
from tkinter import*
from tkinter.ttk import*
from PIL import Image,ImageTk 
import tkinter as tk

window= Tk()
window.title("Circuit Simulator")
window.geometry('700x300')

circuit = {}
circuit1 = {}
circuit2 = {}
circuit3 = {}

def function():
    circuit[len(circuit)] = {"Type":components.get() , "Value":val.get() , "Units":units.get(), "Row":roww.get(),"Coll":coll.get() }
    print(circuit)
##########################
def function1():
    circuit1[len(circuit1)] = {"Type":components1.get() , "Value":val1.get() , "Units":units1.get(), "Row":roww1.get(),"Coll":coll1.get(), "Frequency":freqq1.get(), "FrequencyUnit":frequnit1.get() }
    print(circuit1)
##########################
def function2():
    circuit2[len(circuit2)] = {"Type":components2.get() , "Value":val2.get() , "Units":units2.get(), "Row":roww2.get(),"Coll":coll2.get(), "Frequency":freqq2.get(), "FrequencyUnit":frequnit2.get() }
    print(circuit2)
#########################
def function3():
    circuit3[len(circuit3)] = {"Type":components3.get() , "Value":val3.get() , "Units":units3.get(), "Row":roww3.get(),"Coll":coll3.get(), "Frequency":freqq3.get(), "FrequencyUnit":frequnit3.get() }
    print(circuit3)
##########################
def GoToCircuit(): 
    circuitWindow11 = Toplevel(window)
    circuitWindow11.title("Circuit Diagram")

    resistor = Image.open("RESISTOR.png").resize((100,100))
    img = ImageTk.PhotoImage(resistor)
     
    dcVoltage = Image.open("dcSUPPLY.png").resize((100,100))
    imgg1 = ImageTk.PhotoImage(dcVoltage)
    
    ground = Image.open("Symbol G7_Earth.jpg").resize((100,100))
    imgg2 = ImageTk.PhotoImage(ground)
    
    ac_voltage = Image.open("acSUPPLY.png").resize((100,100))
    img3 = ImageTk.PhotoImage(ac_voltage)

    dcCurrent = Image.open ("DCcurrent.jpeg").resize((100,100))
    img6 = ImageTk.PhotoImage(dcCurrent)
    
    for i in range (0,len(circuit)):
        Picture = ""
        if circuit [i]['Type'] == "Resistor (Ω)":
            Picture = img
            comp1 = tk.Button(circuitWindow11,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])
            
        elif circuit [i]['Type'] == "DC Voltage (V)":
            Picture = imgg1
            comp2= tk.Button(circuitWindow11,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])

        elif circuit [i]['Type'] == "DC Current (A)":
            Picture = img6
            comp2= tk.Button(circuitWindow11,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])

        elif circuit [i]['Type'] == "AC Voltage (V)":
            Picture = img3
            comp2= tk.Button(circuitWindow11,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])   
        
        elif circuit [i]['Type'] == "Ground":
           Picture = imgg2
           comp2= tk.Button(circuitWindow11,image=Picture,highlightthickness=0,bd=0)
           comp2.image = Picture
           comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row']) 
###############################################################################

def GoToCircuit1():

    circuitWindow1 = Toplevel(window)
    circuitWindow1.title("Circuit Diagram")
    
    resistor = Image.open("RESISTOR.png").resize((100,100))
    img = ImageTk.PhotoImage(resistor)
    
    ground = Image.open("Symbol G7_Earth.jpg").resize((100,100))
    imgg2 = ImageTk.PhotoImage(ground)
  
    ac_voltage = Image.open("acSUPPLY.png").resize((100,100))
    img3 = ImageTk.PhotoImage(ac_voltage)
    
    cap = Image.open("capacitoor.jpg").resize((100,100))
    img4 = ImageTk.PhotoImage(cap)

    for i in range (0,len(circuit1)):
        Picture = ""
        if circuit1 [i]['Type'] == "Resistor (Ω)":
            Picture = img
            comp1 = tk.Button(circuitWindow1,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit1[i]['Coll'],row=circuit1[i]['Row'])
            
       
        elif circuit1 [i]['Type'] == "Capacitor (F)":
            Picture = img4
            comp2 = tk.Button(circuitWindow1,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit1[i]['Coll'],row=circuit1[i]['Row'])

        elif circuit1 [i]['Type'] == "AC Voltage (V)":
            Picture = img3
            comp2= tk.Button(circuitWindow1,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit1[i]['Coll'],row=circuit1[i]['Row'])   
        
        elif circuit [i]['Type'] == "Ground":
           Picture = imgg2
           comp2= tk.Button(circuitWindow1,image=Picture,highlightthickness=0,bd=0)
           comp2.image = Picture
           comp2.grid(column=circuit1[i]['Coll'],row=circuit1[i]['Row']) 
############################################################################
def GoToCircuit2():

    circuitWindow2 = Toplevel(window)
    circuitWindow2.title("Circuit Diagram")

    resistor = Image.open("RESISTOR.png").resize((100,100))
    img = ImageTk.PhotoImage(resistor)
     
    ground = Image.open("Symbol G7_Earth.jpg").resize((100,100))
    imgg2 = ImageTk.PhotoImage(ground)
    
    induct = Image.open("INDUCTOR.png").resize((100,100))
    img2 = ImageTk.PhotoImage(induct)
  
    ac_voltage = Image.open("acSUPPLY.png").resize((100,100))
    img3 = ImageTk.PhotoImage(ac_voltage)
    
    cap = Image.open("capacitoor.jpg").resize((100,100))
    img4 = ImageTk.PhotoImage(cap)

    for i in range (0,len(circuit2)):
        Picture = ""
        if circuit2 [i]['Type'] == "Resistor (Ω)":
            Picture = img
            comp1 = tk.Button(circuitWindow2,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit2[i]['Coll'],row=circuit2[i]['Row'])
            
        elif circuit2 [i]['Type'] == "Inductor (H)":
            Picture = img2
            comp1= tk.Button(circuitWindow2,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit2[i]['Coll'],row=circuit2[i]['Row'])
             
        elif circuit2 [i]['Type'] == "Capacitor (F)":
            Picture = img4
            comp2 = tk.Button(circuitWindow2,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit2[i]['Coll'],row=circuit2[i]['Row'])

        elif circuit2 [i]['Type'] == "AC Voltage (V)":
            Picture = img3
            comp2= tk.Button(circuitWindow2,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit2[i]['Coll'],row=circuit2[i]['Row'])   
        
        elif circuit2 [i]['Type'] == "Ground":
           Picture = imgg2
           comp2= tk.Button(circuitWindow2,image=Picture,highlightthickness=0,bd=0)
           comp2.image = Picture
           comp2.grid(column=circuit2[i]['Coll'],row=circuit2[i]['Row']) 
######################################################################
def GoToCircuit3():

    circuitWindow3 = Toplevel(window)
    circuitWindow3.title("Circuit Diagram")

    resistor = Image.open("RESISTOR.png").resize((100,100))
    img = ImageTk.PhotoImage(resistor)
     
    ground = Image.open("Symbol G7_Earth.jpg").resize((100,100))
    imgg2 = ImageTk.PhotoImage(ground)
    
    induct = Image.open("INDUCTOR.png").resize((100,100))
    img2 = ImageTk.PhotoImage(induct)
  
    ac_voltage = Image.open("acSUPPLY.png").resize((100,100))
    img3 = ImageTk.PhotoImage(ac_voltage)

    for i in range (0,len(circuit3)):
        Picture = ""
        if circuit3 [i]['Type'] == "Resistor (Ω)":
            Picture = img
            comp1 = tk.Button(circuitWindow3,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit3[i]['Coll'],row=circuit3[i]['Row'])
            
        elif circuit3 [i]['Type'] == "Inductor (H)":
            Picture = img2
            comp1= tk.Button(circuitWindow3,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])
            

        elif circuit3 [i]['Type'] == "AC Voltage (V)":
            Picture = img3
            comp2= tk.Button(circuitWindow3,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit3[i]['Coll'],row=circuit3[i]['Row'])   
        
        elif circuit3 [i]['Type'] == "Ground":
           Picture = imgg2
           comp2= tk.Button(circuitWindow3,image=Picture,highlightthickness=0,bd=0)
           comp2.image = Picture
           comp2.grid(column=circuit3[i]['Coll'],row=circuit3[i]['Row']) 
###########################################################################

def resis():
    circuitCompWindow = Toplevel(window)
    gridd = Label(circuitCompWindow, text="Choose the circuit components :").grid(column=0,row=1)
    global components
    components= Combobox(circuitCompWindow)
    components.grid(column=0,row=2)
    components ['values'] = ("Resistor (Ω)","DC Voltage (V)","DC Current (A)","AC Voltage (V)","Ground")
    components.current(0) 
    
    choose = Label(circuitCompWindow, text="Choose a Unit")
    choose.grid(column=2,row=1)
    global units
    units= Combobox(circuitCompWindow)
    units.grid(column=2,row=2,padx=10)
    units ['values'] = ("Tera","Giga ","Mega ","kilo ","","Milli ","Micro","Nano","Pico","Femto")
    units.current(0)
    gridd = Label(circuitCompWindow, text="Choose the components coordinates :").grid(column=0,row=5)
    rowww = Label(circuitCompWindow,text="Enter the row's number").grid(column=0,row=6)
    global roww
    roww = Combobox(circuitCompWindow)
    roww.grid(column=1,row=6)
    roww ['values'] = (0,1,2)
    roww.current(0)
    colll = Label(circuitCompWindow,text="Enter the column's number").grid(column=0,row=7)
    global coll
    coll = Combobox(circuitCompWindow)
    coll.grid(column=1,row=7)
    coll ['values'] = (0,1,2)
    coll.current(0)
    r1= Label(circuitCompWindow,text="Enter the values")
    r1.grid(column=1,row=1)
    global val
    val= Entry(circuitCompWindow)
    val.grid(column=1,row=2)
    calc1 = Label(circuitCompWindow, text= "Choose what to calculate: ").grid(column=0, row=9)
    global calacc
    calacc = Combobox(circuitCompWindow)
    calacc ['values'] = ("Current","Voltage")
    calacc.grid(column=1, row=9,pady=10)
    calacc.current(0)
    btn = Button(circuitCompWindow,text="Save Component",command=function)
    btn.grid(column=1,row=10,pady=10)
    cirbtn = Button(circuitCompWindow, text="Circuit Diagram", command=GoToCircuit)
    cirbtn.grid(column=1,row=11)   
        
############################################################################################
def resicap():
    CompWindow = Toplevel(window)
    global components1
    components1= Combobox(CompWindow)
    gridd = Label(CompWindow, text="Choose the circuit components :").grid(column=0,row=1)
    components1.grid(column=0,row=2)
    components1 ['values'] = ("Resistor (Ω)","Capacitor (F)","AC Voltage (V)","Ground")
    components1.current(0) 

    global freqq1
    freq1 = Label(CompWindow,text="Enter the Frequency Value : ")
    freq1.grid(column=0,row=3)
    freqq1 = Entry(CompWindow)
    freqq1.grid(column=0,row=4)
    frequ1 = Label(CompWindow,text="Choose Unit").grid(column=1,row=3)
    global frequnit1
    frequnit1 = Combobox(CompWindow)
    frequnit1.grid(column=1,row=4)
    frequnit1 ['values'] = ("Tera Hz","Giga Hz","Mega Hz","kilo Hz","Hz","Milli Hz","Micro Hz","Nano Hz","Pico Hz","Femto Hz")
    frequnit1.current(0)

    choose = Label(CompWindow, text="Choose a Unit")
    choose.grid(column=2,row=1)
    global units1
    units1= Combobox(CompWindow)
    units1.grid(column=2,row=2,padx=10)
    units1 ['values'] = ("Tera","Giga ","Mega ","kilo ","","Milli ","Micro","Nano","Pico","Femto")
    units1.current(0)
    gridd1 = Label(CompWindow, text="Choose the components coordinates :").grid(column=0,row=5)
    rowww1 = Label(CompWindow,text="Enter the row's number").grid(column=0,row=6)
    global roww1
    roww1 = Combobox(CompWindow)
    roww1.grid(column=1,row=6)
    roww1 ['values'] = (0,1,2)
    roww1.current(0)
    colll1 = Label(CompWindow,text="Enter the column's number").grid(column=0,row=7)
    global coll1
    coll1 = Combobox(CompWindow)
    coll1.grid(column=1,row=7)
    coll1 ['values'] = (0,1,2)
    coll1.current(0)
    r1= Label(CompWindow,text="Enter the values")
    r1.grid(column=1,row=1)
    global val1
    val1= Entry(CompWindow)
    val1.grid(column=1,row=2)
    calc1 = Label(CompWindow, text= "Choose what to calculate: ").grid(column=0, row=9)
    global calacc1
    calacc1 = Combobox(CompWindow)
    calacc1 ['values'] = ("Current","Voltage")
    calacc1.grid(column=1, row=9,pady=10)
    calacc1.current(0)
    btn = Button(CompWindow,text="Save Component",command=function1)
    btn.grid(column=1,row=10,pady=10)

    cirbtn = Button(CompWindow, text="Circuit Diagram", command=GoToCircuit1)
    cirbtn.grid(column=1,row=11)

##############################################################################################
def resindcap():
    circuitComp = Toplevel(window)
    gridd = Label(circuitComp, text="Choose the circuit components :").grid(column=0,row=1)
    global components2
    components2= Combobox(circuitComp)
    components2.grid(column=0,row=2)
    components2 ['values'] = ("Resistor (Ω)","Capacitor (F)","Inductor (H)","AC Voltage (V)","Ground")
    components2.current(0) 
    global freqq2
    freq2 = Label(circuitComp,text="Enter the Frequency Value (if needed)")
    freq2.grid(column=0,row=3)
    freqq2 = Entry(circuitComp)
    freqq2.grid(column=0,row=4)
    frequ2 = Label(circuitComp,text="Choose Unit").grid(column=1,row=3)
    global frequnit2
    frequnit2 = Combobox(circuitComp)
    frequnit2.grid(column=1,row=4)
    frequnit2 ['values'] = ("Tera Hz","Giga Hz","Mega Hz","kilo Hz","Hz","Milli Hz","Micro Hz","Nano Hz","Pico Hz","Femto Hz")
    frequnit2.current(0)

    choose = Label(circuitComp, text="Choose a Unit")
    choose.grid(column=2,row=1)
    global units2
    units2= Combobox(circuitComp)
    units2.grid(column=2,row=2,padx=10)
    units2 ['values'] = ("Tera","Giga ","Mega ","kilo ","","Milli ","Micro","Nano","Pico","Femto")
    units2.current(0)
    
    gridd2 = Label(circuitComp, text="Choose the components coordinates :").grid(column=0,row=5)
    rowww2 = Label(circuitComp,text="Enter the row's number").grid(column=0,row=6)
    global roww2
    roww2 = Combobox(circuitComp)
    roww2.grid(column=1,row=6)
    roww2 ['values'] = (0,1,2)
    roww2.current(0)
    global coll2
    colll2 = Label(circuitComp,text="Enter the column's number").grid(column=0,row=7)
    coll2 = Combobox(circuitComp)
    coll2.grid(column=1,row=7)
    coll2 ['values'] = (0,1,2)
    coll2.current(0)
    r1= Label(circuitComp,text="Enter the values")
    r1.grid(column=1,row=1)
    global val2
    val2= Entry(circuitComp)
    val2.grid(column=1,row=2)
    calc2 = Label(circuitComp, text= "Choose what to calculate: ").grid(column=0, row=9)
    global calacc2
    calacc2 = Combobox(circuitComp)
    calacc2 ['values'] = ("Current","Voltage")
    calacc2.grid(column=1, row=9,pady=10)
    calacc2.current(0)

    btn = Button(circuitComp,text="Save Component",command=function2)
    btn.grid(column=1,row=10,pady=10)
    cirbtn = Button(circuitComp, text="Circuit Diagram", command=GoToCircuit2)
    cirbtn.grid(column=1,row=11)
################################################################################################
def resind():
    circuitWindow = Toplevel(window)
    gridd = Label(circuitWindow, text="Choose the circuit components :").grid(column=0,row=1)
    global components3
    components3= Combobox(circuitWindow)
    components3.grid(column=0,row=2)
    components3 ['values'] = ("Resistor (Ω)","Inductor (H)","AC Voltage (V)","Ground")
    components3.current(0) 
    global freqq3
    freq3 = Label(circuitWindow,text="Enter the Frequency Value (if needed)")
    freq3.grid(column=0,row=3)
    freqq3 = Entry(circuitWindow)
    freqq3.grid(column=0,row=4)
    frequ3 = Label(circuitWindow,text="Choose Unit").grid(column=1,row=3)
    global frequnit3
    frequnit3 = Combobox(circuitWindow)
    frequnit3.grid(column=1,row=4)
    frequnit3 ['values'] = ("Tera Hz","Giga Hz","Mega Hz","kilo Hz","Hz","Milli Hz","Micro Hz","Nano Hz","Pico Hz","Femto Hz")
    frequnit3.current(0)
    choose = Label(circuitWindow, text="Choose a Unit")
    choose.grid(column=2,row=1)
    global units3
    units3= Combobox(circuitWindow)
    units3.grid(column=2,row=2,padx=10)
    units3 ['values'] = ("Tera","Giga ","Mega ","kilo ","","Milli ","Micro","Nano","Pico","Femto")
    units3.current(0)
    gridd3 = Label(circuitWindow, text="Choose the components coordinates :").grid(column=0,row=5)
    rowww3 = Label(circuitWindow,text="Enter the row's number").grid(column=0,row=6)
    global roww3
    roww3 = Combobox(circuitWindow)
    roww3.grid(column=1,row=6)
    roww3 ['values'] = (0,1,2)
    roww3.current(0)
    colll3 = Label(circuitWindow,text="Enter the column's number").grid(column=0,row=7)
    global coll3
    coll3 = Combobox(circuitWindow)
    coll3.grid(column=1,row=7)
    coll3 ['values'] = (0,1,2)
    coll3.current(0)
    r1= Label(circuitWindow,text="Enter the values")
    r1.grid(column=1,row=1)
    global val3
    val3= Entry(circuitWindow)
    val3.grid(column=1,row=2)
    calc1 = Label(circuitWindow, text= "Choose what to calculate: ").grid(column=0, row=9)
    global calacc3
    calacc3 = Combobox(circuitWindow)
    calacc3 ['values'] = ("Current","Voltage")
    calacc3.grid(column=1, row=9,pady=10)
    calacc3.current(0)
    btn = Button(circuitWindow,text="Save Component",command=function3)
    btn.grid(column=1,row=10,pady=10)
    cirbtn = Button(circuitWindow, text="Circuit Diagram", command=GoToCircuit3)
    cirbtn.grid(column=1,row=11)

#################################################

typ = Label(window,text="Choose your Circuit Group: ").grid(column=0,row=6)
typp = Combobox(window)
typp.grid(column=1,row=6)
typp['values'] = ("Series","Parallel")
typp.current(0)
Grouup = typp.get()

btnR = Button(window,text="R",command=resis)
btnR.grid(column=0,row=8)

btnRC = Button(window,text="R-C",command=resicap)
btnRC.grid(column=0,row=9)

btnRL = Button(window,text="R-L",command=resind)
btnRL.grid(column=0,row=10)

btnRLC = Button(window,text="R-L-C",command=resindcap)
btnRLC.grid(column=0,row=11)


window.mainloop()