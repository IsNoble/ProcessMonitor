# ProcessMonitor
Python script to monitor CPU and RAM usage on a given system and publish message to clearblade system via MQTT

TODO

PYTHON
- Add more logging to the script side
- Write proper error handling code for script side failures
- Convert Python timestamp to JavaScript/Clearblade Timestamp object?
- ~~Handle Keyboard Interrupt or similar?~~
    - Completed. Script now cleanly handles KeyboardInterrupts
- ~~Currently opening and connecting and disconnecting MQTT for every message. This is likely inefficient. R&I ~~
    - Completed, Script now connects and disconnects to/from MQTT a single time. 

ClearBlade System
- Get Microservice + Timer working. 
  - creation error :"json: cannot unmarshal bool into Go value of type map[string]interface {}"?
- Convert ProcessLog collection timestamp column to use Timestamp instead of string.
- Put a row limit/row check on ProcessLog Collection? Not sure how resources are allocated to the system, or from where. R&I  
- Script is sending 3 messages at a time???
