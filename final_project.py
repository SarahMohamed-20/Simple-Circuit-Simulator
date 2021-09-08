from tkinter import*
from tkinter.ttk import*
from PIL import Image,ImageTk 
import tkinter as tk

window= Tk()
window.title("Circuit Simulator")
window.geometry('700x300')
r= Label(window, text="Choose the circuit components")
r.grid(column=0,row=1)

circuitWindow = Toplevel()
#circuitWindow = tk.Toplevel(window)
circuitWindow.geometry('700x300')
circuitWindow.title("Circuit Diagram")

##tt7t gowa el function##resultsWindow = Toplevel(circuitWindow)
##resultsWindow.geometry('600x300')

val = StringVar()
units = StringVar()
freqq = StringVar()

circuit = {}
#Curr = {}
#Volt = {}

###########################################################
def function():
    circuit[len(circuit)] = {"Type":components.get() , "Value":val.get() , "Units":units.get(), "Row":roww.get(),"Coll":coll.get(), "Frequency":freqq.get(), "FrequencyUnit":frequnit.get() }
    print(circuit)
############################################################
'''def amm_Store():
    Curr[len(Curr)] = {"AmmeterRow1":ammRoww1.get(), "AmmeterColl1":ammCol1.get(), "AmmeterRow2":ammRoww2.get(), "AmmeterColl2":ammCol2.get(), "AmmeterRow3":ammRoww3.get(), "AmmeterColl3":ammCol3.get(), "AmmeterRow4":ammRoww4.get(), "AmmeterColl4":ammCol4.get(), "AmmeterRow5":ammRoww5.get(), "AmmeterColl5":ammCol5.get() }
    print(Curr)
################################################################
def vol_Store():
    Volt[len(Volt)] =  {"VoltameterRow1":voltaRow1.get(), "VoltamenterColl1":voltaCol1.get(), "VoltameterRow2":voltaRow2.get(), "VoltamenterColl2":voltaCol2.get(),"VoltameterRow3":voltaRow3.get(), "VoltamenterColl3":voltaCol3.get(),"VoltameterRow4":voltaRow4.get(), "VoltamenterColl4":voltaCol4.get(), "VoltameterRow5":voltaRow5.get(), "VoltamenterColl5":voltaCol5.get()}
    print (Volt)
'''###############################################################
'''def Calculations():
    #for i in range (0,len(Curr),-1):

    if ammRoww1 != '-' and ammCol1 != '-':
        a = ammRoww1.get()
        ac = ammCol1.get()
        for i in range (0,len(circuit)):
            if circuit [i]['Row'] == a and circuit [i]['Coll'] == ac:

                
'''
T = {x:{i:None for i in range(4)} for x in range(4)}

def GoToCircuit():

    photo = Image.open("1646bread1.png").resize((600,300))
    pto = ImageTk.PhotoImage(photo)
    background = Label(circuitWindow, image=pto)
    background.image = photo

    resistor = Image.open("RESISTOR.png").resize((100,100))
    img = ImageTk.PhotoImage(resistor)
     
    dcVoltage = Image.open("dcSUPPLY.png").resize((100,100))
    imgg1 = ImageTk.PhotoImage(dcVoltage)
    
    ground = Image.open("Symbol G7_Earth.jpg").resize((100,100))
    imgg2 = ImageTk.PhotoImage(ground)
    
    induct = Image.open("INDUCTOR.png").resize((100,100))
    img2 = ImageTk.PhotoImage(induct)
  
    ac_voltage = Image.open("acSUPPLY.png").resize((100,100))
    img3 = ImageTk.PhotoImage(ac_voltage)

    dcCurrent = Image.open ("DCcurrent.jpeg").resize((100,100))
    img6 = ImageTk.PhotoImage(dcCurrent)
    
    cap = Image.open("capacitoor.jpg").resize((100,100))
    img4 = ImageTk.PhotoImage(cap)

    for i in range (0,len(circuit)):
        Picture = ""
        if circuit [i]['Type'] == "Resistor (Ω)":
            Picture = img
            comp1 = tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])
            
        elif circuit [i]['Type'] == "Inductor (H)":
            Picture = img2
            comp1= tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
            comp1.image = Picture
            comp1.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])
             
        elif circuit [i]['Type'] == "Capacitor (F)":
            Picture = img4
            comp2 = tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])

        elif circuit [i]['Type'] == "DC Voltage (V)":
            Picture = imgg1
            comp2= tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])

        elif circuit [i]['Type'] == "DC Current (A)":
            Picture = img6
            comp2= tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])

        elif circuit [i]['Type'] == "AC Voltage (V)":
            Picture = img3
            comp2= tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
            comp2.image = Picture
            comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])   
        
        elif circuit [i]['Type'] == "Ground":
           Picture = imgg2
           comp2= tk.Button(circuitWindow,image=Picture,highlightthickness=0,bd=0)
           comp2.image = Picture
           comp2.grid(column=circuit[i]['Coll'],row=circuit[i]['Row'])  

    ###########################
    

meters = Label(circuitWindow, text = "Enter the Node of your Chosen Meter : ")
meters.grid(column=0,row=6)
'''
Rows = Label(circuitWindow, text=" Row Number").grid(column=2,row=7)
Columns = Label(circuitWindow, text=" Column Number").grid(column=3,row=7)

Rowss = Label(circuitWindow, text=" Row Number").grid(column=6,row=7)
Columnss = Label(circuitWindow, text=" Column Number").grid(column=7,row=7)
'''

#vols = Button(circuitWindow,text= "Save Voltmeters",command= vol_Store).grid(column=6, row=13)

###########################################################################################
components= Combobox(window)
components.grid(column=0,row=2)
components ['values'] = ("Resistor (Ω)","Capacitor (F)","Inductor (H)","DC Voltage (V)","DC Current (A)","AC Voltage (V)","Ground")
components.current(0) 

freq = Label(window,text="Enter the Frequency Value (if needed)")
freq.grid(column=0,row=3)
freqq = Entry(window)
freqq.grid(column=0,row=4)
frequ = Label(window,text="Choose Unit").grid(column=1,row=3)
frequnit = Combobox(window)
frequnit.grid(column=1,row=4)
frequnit ['values'] = ("Tera Hz","Giga Hz","Mega Hz","kilo Hz","Hz","Milli Hz","Micro Hz","Nano Hz","Pico Hz","Femto Hz")
frequnit.current(0)

choose = Label(window, text="Choose a Unit")
choose.grid(column=2,row=1)
units= Combobox(window)
units.grid(column=2,row=2,padx=10)
units ['values'] = ("Tera","Giga ","Mega ","kilo ","","Milli ","Micro","Nano","Pico","Femto")
units.current(0) 
################################################################################################

gridd = Label(window, text="Choose the components coordinates :").grid(column=0,row=5)
rowww = Label(window,text="Enter the row's number").grid(column=0,row=6)
roww = Combobox(window)
roww.grid(column=1,row=6)
roww ['values'] = (0,1,2)
roww.current(0)

coll = Label(window,text="Enter the column's number").grid(column=0,row=7)
coll = Combobox(window)
coll.grid(column=1,row=7)
coll ['values'] = (0,1,2)
coll.current(0)
    
r1= Label(window,text="Enter the values")
r1.grid(column=1,row=1)
val= Entry(window)
val.grid(column=1,row=2)

btn = Button(window,text="Save Component",command=function)
btn.grid(column=1,row=8,pady=10)

cirbtn = Button(window, text="Circuit Diagram", command=GoToCircuit)
cirbtn.grid(column=1,row=9)

######################################################################################

####################################################################################
window.mainloop()