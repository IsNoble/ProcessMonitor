# ProcessMonitor
Python script to monitor CPU and RAM usage on a given system and publish message to clearblade system via MQTT

TODO

PYTHON
- Add more logging to the script side
- Write error handling code for script side failures
- Convert Python timestamp to JavaScript/Clearblade Timestamp object?

ClearBlade System
- Get Microservice + Timer working. 
  - creation error :"json: cannot unmarshal bool into Go value of type map[string]interface {}"?
- Convery ProcessLog collection timestamp column to use Timestamp instead of string.
- Put a row limit/row check on ProcessLog Collection. 
- Double check the collection is not getting double updated when the Python script initial starts publishing messages. 
