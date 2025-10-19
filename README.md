# The reborn of a casio mini TV-800

This repository is intended to track the transformation of a casio mini tv into a portable clock and usefull device. I have purchased this damaged tv to remove all the screen and damaged pcb, to add a ESP Wroom 32 D1 with a MAX98357A digital I2S Class D amplifier, and a cheap 1.8 inch screen with resolution of 128x160 pixels.

## Components used:

* Broken Casio TV-800.
* ESP Wroom 32 D1.
* MAX98357A digital I2S Class D amplifier.
* Small ~ 1.5cm speaker, in parallel to the original speaker of the mini tv.
* Female USB-C, to feed 5v to the ESP32.
* Switch to turn off the main board, breaking the + of the USB-C Cable.
* ST7735S of 1.8 inch screen, with a 128x160 pixels.
* A lot of wires.

Basic soldering skills were needed to join and wire the cables.

The board was flashed with Micropython "ESP32_GENERIC-20250911-v1.26.1.bin" firmware.

## About the Casio tv-800:

Its a nice cube-shaped  TV - Ultra-Compact according to an advert from 1987. Only 47 mm screen size, 360 g with 4 AA-size batteries. Made in Japan.

## Reference image of the original case

![Image of the casio tv-800](https://raw.githubusercontent.com/leitzzz/mini_tv_reborn/16e43093a75c8c3a67a2468d36297b9ac6690145/casio_tv800/tv-800-gr.jpg "Casio tv-800")

