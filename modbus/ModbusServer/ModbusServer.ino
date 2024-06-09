#include <Modbus.h>
#include <ModbusIP.h>
#include <SPI.h>

int tanklevel;
int tanklevel_old;

const int ir = 100;

//Modbus IP Object
ModbusIP mb;

void setup() {
  Serial.begin(9600);
  // MAC and IP address config
  byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };  
  byte ip[] = { 192, 168, 0, 177 };    
  mb.config(mac, ip);

  // Add input register and write a dummy variable
  mb.addIreg(ir);
  tanklevel = 12;
  mb.Ireg(ir, tanklevel);
}

void loop() {
  mb.task();
  String tmpstr;
  tmpstr = "Tank Level: " + String(tanklevel) + " ft";
  Serial.println(tmpstr);
  delay(1000);
}
