import machine
import time
import ntptime

from screen.st7735 import TFT
from screen.sysfont import sysfont

from config.config import GENERAL_CONFIG, WIFI_PARAMETERS, TFT_PARAMETERS, WAV_AUDIOS, BIOS_INFO

from sound.sound import sound
from wifi.wifi import connect_wifi
from screen.screen import screen_instance
from tools import clock, bios_checking, weather


def main():
    # vars init
    weather_data = None
    started_at_ts = time.time()

    screen_instance.clear()

    # bios simulation init
    bios_checking.bios_check(BIOS_INFO, screen_instance.tft)
    # play audio sound, to simulate old pc BIOS beep, im that old school mood.
    # sound.play_sound(WAV_AUDIOS["bios_beep"], screen_instance.tft)
    time.sleep(5)
    screen_instance.clear()

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

        # only try to fetch weather data if wifi is connected, otherwise it will raise an error, and we will show the error message on the screen.
        try:
            # fetch weather data based in the city coordinates, you can change it to any city you want by changing the latitude and longitude values.
            weather_data = weather.fetch_weather_data(
                city_coords=(GENERAL_CONFIG["your_city"]["latitude"], GENERAL_CONFIG["your_city"]["longitude"]))
        except Exception as e:
            print(f"Error fetching weather data: {e}")
    else:
        print("WIFI Connection Failed!")

        # play audio error sound X times.
        for _ in range(3):
            sound.play_sound(WAV_AUDIOS["error"], screen_instance.tft)
            time.sleep(1)

        screen_instance.tft.text((0, 20), "WIFI Connection Failed!",
                                 TFT.RED, sysfont, 1, nowrap=True)

    # if weather_data:
    #     print("Weather data fetched successfully:")
    #     print(weather_data)

    # main logo display
    # fill screen with white color, before showing the logo.
    screen_instance.fill_with_color(TFT.WHITE)
    screen_instance.show_image(
        'assets/images/casio.bmp', TFT_PARAMETERS["screen_disposition_width"], TFT_PARAMETERS["screen_disposition_height"])
    time.sleep(5)
    screen_instance.clear()

    # if timeout is set, reboot the device after the specified time
    if (GENERAL_CONFIG["reboot_after_no_wifi_connection"] > 0):
        screen_instance.tft.text((0, 30), f"Will reboot in {GENERAL_CONFIG['reboot_after_no_wifi_connection']} seconds",
                                 TFT.RED, sysfont, 1, nowrap=True)
        time.sleep(GENERAL_CONFIG["reboot_after_no_wifi_connection"])
        machine.reset()

    time.sleep(1)

    # synchronize RTC via NTP
    ntptime.settime()

    # add the location name to the weather data, so we can show it on the screen, if weather_data is None, the show_weather function will handle it and show a message on the screen.
    if weather_data is not None:
        weather_data["location"] = GENERAL_CONFIG["your_city"]["name"]

    while True:
        # show clocks for different countries
        for country, offset in GENERAL_CONFIG["countries_to_get_time"]:
            screen_instance.clear()
            clock.show_clock(screen_instance.tft,
                             ts_offset=offset, subtitle=country)
            time.sleep(1)

        screen_instance.clear()

        weather.show_weather(screen_instance.tft, weather_data)
        time.sleep(10)

        # after 3 minutes, break the loop and end the program, you can change this value to any time you want.
        if time.time() - started_at_ts > GENERAL_CONFIG["reboot_after_seconds"]:
            # reset the device to start again from the beginning.
            machine.reset()

        # time.sleep(2)

    # play audio sound
    # sound.play_sound(WAV_AUDIOS["chimes"], screen_instance.tft)

    # Clean up the I2S peripheral
    # sound.deinit_audio()
    # print("I2S de-initialized.")


if __name__ == "__main__":
    main()
