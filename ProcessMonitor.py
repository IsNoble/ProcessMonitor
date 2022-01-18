import json
import datetime
import time
import psutil                       #pip install psutil
import clearblade_adapter_library   #pip install clearblade

timerLength = 59 #59 + 1 second interval for the CPU percentage = 60 second timer.

def ProcessMonitor():

    #Initilization
    Adapter = clearblade_adapter_library.AdapterLibrary('Adapter')
    Adapter.parse_arguments()
    Adapter.initialize_clearblade()
    #Connect to clearblade system
    Adapter.connect_MQTT("ProcessMonitorData")

    while True:
        try:
            #JSON testjson Data capture & construction
            timestamp = datetime.datetime.now().strftime("%b %d, %Y - %H:%M:%S")
            CPU = psutil.cpu_percent(interval=1)
            RAM = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)
            processdata = json.dumps({'timestamp':timestamp, 'ram_usage_percentage':RAM, "cpu_usage_percentage":CPU})
            #Publish processdata
            Adapter.publish("ProcessMonitorData", processdata)
            time.sleep(timerLength)
        except KeyboardInterrupt:
            break
    #Disconnect from clearblade system
    Adapter.disconnect_MQTT()


ProcessMonitor()
