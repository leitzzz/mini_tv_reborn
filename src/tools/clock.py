import time
from screen.st7735 import TFT
from screen.sysfont import sysfont


def show_clock(tft, ts_offset=0, subtitle=""):

    ts = time.time() + ts_offset

    current_time = time.localtime(ts)  # get local time tuple

    # show time on the screen
    tft.text((0, 10), str(current_time[3]) + ":" + str(current_time[4]) +
             ":" + str(current_time[5]), TFT.GREEN, sysfont, 3, nowrap=True)
    tft.text((0, 40), subtitle, TFT.GREEN, sysfont, 2, nowrap=True)
