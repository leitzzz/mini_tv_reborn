import machine
import time
import ntptime

from screen.st7735 import TFT
from screen.sysfont import sysfont

from config.config import GENERAL_CONFIG, WIFI_PARAMETERS, TFT_PARAMETERS, WAV_AUDIOS, BIOS_INFO

from sound.sound import sound
from wifi.wifi import connect_wifi
from screen.screen import screen_instance
from tools import clock, bios_checking


def main():
    screen_instance.clear()

    # bios simulation init
    # bios_checking.bios_check(BIOS_INFO, screen_instance.tft)
    # play audio sound, to simulate old pc BIOS beep, im that old school mood.
    # sound.play_sound(WAV_AUDIOS["bios_beep"], screen_instance.tft)
    # time.sleep(10)
    # screen_instance.clear()

    # main logo display
    # fill screen with white color, before showing the logo.
    # screen_instance.fill_with_color(TFT.WHITE)
    # screen_instance.show_image(
    #     'assets/images/casio.bmp', TFT_PARAMETERS["screen_disposition_width"], TFT_PARAMETERS["screen_disposition_height"])
    # time.sleep(5)
    # screen_instance.clear()

    wifi_handle = connect_wifi(
        WIFI_PARAMETERS["ssid"], WIFI_PARAMETERS["password"])

    # You can use the wifi_handle later to check status or get IP.
    if wifi_handle.isconnected():
        print("Ready to use internet services.")

        ifconfig = wifi_handle.ifconfig()  # network connection info

        screen_instance.tft.text((0, 10), "Connected!",
                                 TFT.GREEN, sysfont, 2, nowrap=True)
        screen_instance.tft.text((0, 40), f"Local IP: {ifconfig[0]}",
                                 TFT.GREEN, sysfont, 1, nowrap=True)
    else:
        print("WIFI Connection Failed!")

        # play audio error sound X times.
        for _ in range(3):
            sound.play_sound(WAV_AUDIOS["error"], screen_instance.tft)
            time.sleep(1)

        screen_instance.tft.text((0, 20), "WIFI Connection Failed!",
                                 TFT.RED, sysfont, 1, nowrap=True)

        # if timeout is set, reboot the device after the specified time
        if (GENERAL_CONFIG["reboot_after_no_wifi_connection"] > 0):
            screen_instance.tft.text((0, 30), f"Will reboot in {GENERAL_CONFIG['reboot_after_no_wifi_connection']} seconds",
                                     TFT.RED, sysfont, 1, nowrap=True)
            time.sleep(GENERAL_CONFIG["reboot_after_no_wifi_connection"])
            machine.reset()

    time.sleep(3)

    ntptime.settime()

    for _ in range(10):
        screen_instance.clear()
        clock.show_clock(screen_instance.tft, ts_offset=-
                         14400, subtitle="UTC-4")
        time.sleep(0.5)

    time.sleep(2)

    # play audio sound
    # sound.play_sound(WAV_AUDIOS["chimes"], screen_instance.tft)

    # Clean up the I2S peripheral
    sound.deinit_audio()
    # print("I2S de-initialized.")


if __name__ == "__main__":
    main()
