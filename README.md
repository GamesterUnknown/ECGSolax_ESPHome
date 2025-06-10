# ECGSolax_ESPHome
ESPHome example configuration to monitor and control a ECGSolax 6.2kWt inverter via RS232.

This is updated version of https://github.com/syssi/esphome-pipsolar

# Requirements
* ESPHome 2024.6.0 or higher.
* One half of an ethernet cable with RJ45 connector.
* RS232-to-TTL module (MAX3232CSE f.e.)
* Generic ESP32.

### ESP8266 
This configuration can be used on the ESP8266, but you won't be able to use all the sensors due to the memory limitations of the ESP8266. 
You can use minimal set of sensors/selects, leaving only the ones you need. You can use "Heap size" sensor of Debug module to determine how much free memory left. 
Looks like minimum heap size, that ensures stability, is near 6Kb. Although I still strongly recommend using ESP32.
Also Ota upgrade might be failed due to absent of EEPROM memory for downloading update. In such case use USB or WEB firmare update.

### Original Monitoring Stick
The original monitoring stick looks like use ESP8266 and MAX3232, and probably can be reflashed to ESPHome via pins on the board.

# RJ45 connector

```
               RS232                     UART-TTL
┌──────────┐              ┌──────────┐                ┌─────────┐
│          │              │          │<----- RX ----->│         │
│          │<---- TX ---->│  RS232   │<----- TX ----->│ ESP32   │
│   ECG    │<---- RX ---->│  to TTL  │<----- GND ---->│         │
│  Solax   │              │  module  │<-- 3.3V VCC -->│         │
│          │<---- GND --->│          │       │        │         │
│ Inverter │       │      └──────────┘       │        └─────────┘
│          │       │      ┌──────────┐       │
│          │       │----->│   DC-DC  │       │
│          │<- VCC 12V -->│          │-3.3V->│
└──────────┘              └──────────┘
```

| Pin     | Purpose      | MAX3232 pin       | Color T-568B |
| :-----: | :----------- | :---------------- | :------------|
|    1    |              |                   |              |
|    2    | VCC 12V      |                   | Orange       |
|    3    | TX           | P13 (RIN1)        | White-Green  |
|    4    |              | -                 |              |
|    5    | GND          | P15 (GND)         |  White-Blue  |
|    6    | RX           | P14 (DOUT1)       |  Green       |
|    7    |              |                   |              |
|    8    |              |                   |              |

VCC 12V can be used to power up ESP32 and Max3232 via 360Mini, AMS1117-3.3 or similar DC-DC power board converting 12V to 3.3V  

# References
* https://github.com/syssi/esphome-pipsolar
* https://github.com/esphome/esphome/pull/1664
* https://github.com/esphome/esphome-docs/pull/1084/files
* https://github.com/andreashergert1984/esphome/tree/feature_pipsolar_anh
* https://github.com/jblance/mpp-solar/tree/master/docs/protocols
