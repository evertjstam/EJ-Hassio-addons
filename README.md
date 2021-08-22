# Home Assistant Add-on: GPIO RF Sniffer 2MQTT

Reads radio frequency signal codes off of a Raspberry Pi GPIO pin. Sniffed codes are logged and published in mqtt broker in sensors/rf/receiver

Set following in configuration for mqtt
    "mosquitto_address": "str",
    "mosquitto_port": "int",
    "mosquitto_user": "str",
    "mosquitto_password": "str" 

![GPIO pin layout][gpio-pins]

This add-on provides a simple way to read the radio frequency codes from a GPIO pin of a Raspberry Pi wired with generic 433/315MHz capable modules.

![RF hardware][rf-hardware]

Uses the Python library [rpi-rf-gpiod] and adjusted script rpi-rf_receive .  More details about wiring and hardware can be found on the [rpi-rf-gpiod] site.

This add-on has been tested with a RPi 4b running [Home Assistant] and will probably work with a 3b/3b+ .

![Supports armv7 Architecture][armv7-shield]

[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[rpi-rf-gpiod]: https://pypi.org/project/rpi-rf-gpiod/
[gpio-pins]: https://github.com/darthsebulba04/hassio-gpio-rf/raw/master/GPIO.png
[rf-hardware]: https://github.com/darthsebulba04/hassio-gpio-rf/raw/master/rf-boards.png
[Home Assistant]: https://www.home-assistant.io
