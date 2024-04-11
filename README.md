# IOx-hosted Parani SD1000 Bluetooth Scanner

Utilising the PySerial library, AT commands are sent to the Parani SD1000 over RS232 connection. A specialised RJ45-to-RS232 adapter is required for use on the native serial port (which is DTE) of the IR1101.

## Adapter Pinouts
Parani DCE to IR1101 DTE

| Parani DB9 | IR1101 RJ45 | Adapter RJ45 colour |
|------------|-------------|---------------------|
| 1          | 2           | Orange              |
| 2          | 5           | Green               |
| 3          | 6           | Yellow              |
| 4          | 3           | Black               |
| 5          | 4           | Red                 |
| 6          | 1           | Blue                |
| 7          | 8           | White               |
| 8          | 7           | Brown               |
| 9          | N/A         | N/A                 |

## IR1101 Configuration SETUP, REQS, DHCP FOR DYNAMIC ADDRESSING, ETC

## Design of Software Functionality

The originally designed AT command state machine is quite primitive but fully achieves the goal of putting the device's state into Standby, and capturing the surrounding device's Bluetooth MAC addresses.

INSERT AT COMMAND STATE MACHINE

However, this is only a glance into the final flow of the software, as many more features have been added since this initial design of the process. A full insight into the working of the software can be seen below.

INSERT FULL STATE MACHINE

## Implementation TALK MORE ABOUT THE SPECIFIC STUFF

## Protocols (IMP, OMP, ETC)

The transmission of the Bluetooth MAC addresses and timestamp pairs require a specialised 22-byte long packet format to be crafted and packed. A pair can only be transmitted via a single packet, i.e. there are no chaining of records into a single packet. The name of this protocol is the Incoming Message Protocol, its responsiblility is to structure the data for the external server-side processing.

There is also a heartbeat packet, in which the Bluetooth MAC address is set to twelve ASCII space characters ("            "). This is used in times of low traffic, to ensure the hardware has not become faulty and is still functioning.

PROTOCOL IMAGE

| Parani DB9 | IR1101 RJ45 | Adapter RJ45 colour |
|----|---|---|
| TEST |
| 2 | 5 | Green |
| 3 | 6 | Yellow |
| 4 | 3 | Black |
| 5 | 4 | Red |
| 6 | 1 | Blue |
| 7 | 8 | White |
| 8 | 7 | Brown |
| 9 | N/A | N/A |

## Issues
