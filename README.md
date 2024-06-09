## Arduino - Modbus
This repo contains some examples to run a regular webserver or a Modbus server or client on an Arduino UNO with an Ethernet module.

# TODO
- Arduino as Modbus client with Modbus server running in Python
- Test connectivity reliability using Modbus CRC 
- Use standard Arduino Modbus library

Note to self: the main culprit with connectivity issues is IP addressing. When connecting the Ethernet switch, I don't use DHCP (maybe I should?) and instead set my IP address manually. I have used 

- 192.168.1.100 
- 192.168.0.100 

successfully, both with a subnet mask of 255.255.255.0, meaning I can assign the Arduino any IP address in the third octet, e.g. 192.168.1.177 or 192.168.1.100. 

## Additional libraries
The ModbusServer uses Modbus.h and ModbusIP.h - these are files I downloaded from the internet as opposed to the standard ArduinoModbus library. I have them at `/Users/maurits/Documents/Arduino/libraries/`, see `c_cpp_properties.json`.