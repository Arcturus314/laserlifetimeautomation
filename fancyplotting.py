import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as sg

startat = 1500
skip  = 100
uselabels = True

plt.figure(figsize=(15,10))

def get_info(lednum):
    # reads from labels at index lednum+1
    labels = pd.read_csv("Copy of 8_channel_list.csv")
    ledlabel = str(labels[labels["ch"] == lednum+1])
    line1, line2 = ledlabel.split("\n")
    heads = [el for el in line1.split(" ") if el != '']
    dats  = [el for el in line2.split(" ")[1:] if el != '' ]    
    output = ""
    for h,d in zip(heads, dats): output += h+": "+d+" "
    return output

    
def butterplot_norm(filename, lednum):
    
    cutoff = 5e-2
    filtb, filta = sg.butter(1, cutoff)
    
    print("loading data for",filename)
    data     = pd.read_csv(filename)
    print("-filtering")
    filtered = sg.filtfilt(filtb, filta, data["voltage"])[startat::skip]
    xvals = [(time-data["time"][0])/3600 for time in data["time"]][startat::skip]
    yvals = [el/max(filtered) for el in filtered[:len(data["voltage"])]]
    print("-plotting")
    
    if uselabels: plt.plot(xvals, yvals, label=get_info(lednum))
    else: plt.plot(xvals, yvals)

for i in range(8):
    butterplot_norm("lifetimedata/logLED"+str(i)+".csv", i)
    
plt.title("Filtered / Normalized LED Lifetime")
plt.xlabel("Time (hours)")
plt.ylabel("Normalized Photodetector Voltage")
plt.grid()
plt.gca().set_axisbelow(True)
plt.legend()
plt.savefig("lifetimes.png", dpi=600)
plt.show()
