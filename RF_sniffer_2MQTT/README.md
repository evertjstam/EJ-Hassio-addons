# Home Assistant Add-on: RF sniffer 2MQTT

Reads radio frequency signal codes off of a Raspberry Pi GPIO pin. Sniffed codes are logged and published in mqtt broker in sensors/rf/receiver

Set following in configuration for mqtt

"mosquitto_address": "str",

"mosquitto_port": "int",

"mosquitto_user": "str",

"mosquitto_password": "str",

"mosquitto_topic": "str"

This add-on provides a simple way to read the radio frequency codes from a GPIO pin of a Raspberry Pi wired with generic 433/315MHz capable modules.

Uses the Python library [rpi-rf-gpiod] and adjusted script rpi-rf_receive .  More details about wiring and hardware can be found on the [rpi-rf-gpiod] site.

This add-on has been tested with a RPi 4b running [Home Assistant] and will probably work with a 3b/3b+ .

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[rpi-rf-gpiod]: https://pypi.org/project/rpi-rf-gpiod/
[Home Assistant]: https://www.home-assistant.io

