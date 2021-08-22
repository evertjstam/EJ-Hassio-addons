#!/usr/bin/env python3

import argparse
import signal
import sys
import time
import logging
import gpiod
import os
import json

#mosquitto_address = "192.168.86.161"
#mosquitto_port = "1883"
#mosquitto_user = "mqtt"
#mosquitto_password = "mqtt" 

f = open('/data/options.json', 'r')

config = json.loads(f.read())

f.close

logging.info(config)

from rpi_rf_gpiod import RFDevice

rfdevice = None

# pylint: disable=unused-argument
def exithandler(signal, frame):
    sys.exit(0)

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s', )

parser = argparse.ArgumentParser(description='Receives a decimal code via a 433/315MHz GPIO device')
parser.add_argument('-g', dest='gpio', type=int, default=27,
                    help="GPIO pin (Default: 27)")
args = parser.parse_args()

basecode = None
signal.signal(signal.SIGINT, exithandler)

with gpiod.Chip("gpiochip0") as chip:
    gpio = chip.get_line(args.gpio)
    gpio.request(consumer="rpi-rf_receive", type=gpiod.LINE_REQ_EV_BOTH_EDGES)
    rfdevice = RFDevice(gpio)
    timestamp = None
    logging.info("Listening for codes on GPIO " + str(args.gpio))
    try:
        while True:
            ev_gpio = gpio.event_wait(sec=1)
            if ev_gpio:
                event = gpio.event_read()
                rfdevice.rx_callback()
                timestamp = rfdevice.rx_code_timestamp
                if rfdevice.rx_code != basecode:
                    logging.info(str(rfdevice.rx_code) +
                            " [pulselength " + str(rfdevice.rx_pulselength) +
                            ", protocol " + str(rfdevice.rx_proto) + "]")
                    os.system("mosquitto_pub -V mqttv311 -h " + config.mosquitto_address + " -p " + config.mosquitto_port + " -t 'sensors/rf/receiver' -u " + config.mosquitto_user + " -P " + config.mosquitto_password + " -m " + str(rfdevice.rx_code))
                    basecode = rfdevice.rx_code
    except KeyboardInterrupt:
        sys.exit(130)