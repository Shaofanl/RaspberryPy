RaspberryPy
---

My python toolkits for Raspberry Pi Model 3 B, and the operating system is Linux raspberrypi 4.4.26-v7+


Dependences
---

- [RPi](Installed by default in Raspbian)
- [Neopixel for Raspberry pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/software) (Only required in display.Neopixel)
- [Flask](http://flask.pocoo.org/) (Only required in application.motion\_monitor)
- pySerial, enum34 (Only required in control.Myo)
- netifaces (Required in `applications/ip_lcd.py`



Applications
---

- motion\_lcd.py (Display the acceleration and gyroscope to the LCD dynamically)
- motion\_monitor.py (Display the acceleration, gyroscope, and temperature to a webpage dynamically.)
