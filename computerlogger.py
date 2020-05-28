import matplotlib.pyplot as plt
import ledmodel
import arduinointerface
import time

log_dir    = "lifetimelogging"
log_prefix = "logLED"
numLED = 8

LEDs = []
logger = arduinointerface.ArduinoInterface("/dev/ttyACM0", numLED)

for i in range(numLED): LEDs.append(ledmodel.LEDModel(log_dir+"/"+log_prefix+str(i)+".csv", i))

num_samples = 0

while True:

    num_samples += 1

    led_status = logger.update()

    if led_status != 0:

        for identifier, voltage in led_status:
            LEDs[identifier].add_data(voltage, time.time())

        if num_samples % 60 == 0:
            for led in LEDs: led.plot()
            print("\n")

    else: print("Received incomplete data")
