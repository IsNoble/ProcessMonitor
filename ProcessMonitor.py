import os
import json
import datetime
import threading
import psutil                       #pip install psutil
import clearblade_adapter_library   #pip install clearblade

timerLength = 59 #59 + 1 second interval for the CPU percentage = 60 second timer.

def ProcessMonitor():
    #JSON Data capture
    timestamp = datetime.datetime.now().strftime("%b %d, %Y - %H:%M:%S")
    CPU = psutil.cpu_percent(interval=1)
    RAM = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)

    #JSON Data formating & construction
    testjson = json.dumps({'timestamp':timestamp, 'ram_usage_percentage':RAM, "cpu_usage_percentage":CPU})

    #ClearBlade Messaging
    Adapter = clearblade_adapter_library.AdapterLibrary('Adapter')
    Adapter.parse_arguments()
    Adapter.initialize_clearblade()
    Adapter.connect_MQTT("TestTopic")
    Adapter.publish("ProcessMonitorData", testjson)
    Adapter.disconnect_MQTT()
    threading.Timer(timerLength, ProcessMonitor).start()

ProcessMonitor()
