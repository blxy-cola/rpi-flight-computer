# the program i used to test the functionality of the GPS module, luckily it was simpler than i thought!
# i can successfuly deduce that the GPS feature is working so far and i can move on to testing the next thing

# it's important to note that, at least for now (maybe a problem with lame wires), the stability of connection is a bit finnicky. 
# it takes ~10 minutes to find connections and warm up, and then a lot of times will oscillate between outputs of gps data and having no data between each tick of print()'s.
# so far, it's not an issue as long as it still provides gps data generally, because the gps is most helpful when recovering the rocket and obtaining exact height at times to
# account for drifting data in other sensors.

from machine import Pin, UART
import time
import gps_parser

# GPS UART setup
gps_uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Create GPS reader object
gps = gps_parser.GPSReader(gps_uart)

while True:
    # obtain gps data / read any new gps data
    gps_data = gps.get_data()
    
    print("Has Fix: " + str(gps_data.has_fix), "Lat: " + str(gps_data.latitude), "Lon: " + str(gps_data.longitude), "Alt: " + str(gps_data.altitude) + " m  ", "Sat #: " + str(gps_data.satellites))
    
    time.sleep(1)
