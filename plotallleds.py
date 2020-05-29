import matplotlib.pyplot as plt
import pandas as pd
import scipy.signal as sg

num_leds = 8

plt.figure(figsize=(10,7))
    
def butterplot_norm(filename):
    
    cutoff = 5e-2
    filtb, filta = sg.butter(1, cutoff)
    
    data     = pd.read_csv(filename)
    filtered = sg.filtfilt(filtb, filta, data["voltage"])

    plt.plot([ (time-data["time"][0])/86400 for time in data["time"]], [el/max(filtered) for el in filtered[:len(data["voltage"])]], label=filename)

for i in range(num_leds):
    butterplot_norm("lifetimelogging/logLED"+str(i)+".csv")
    
plt.title("Filtered / Normalized LED Lifetime")
plt.xlabel("Time (days)")
plt.ylabel("Normalized Photodetector Voltage")
plt.grid()
plt.gca().set_axisbelow(True)
plt.legend()
plt.show()