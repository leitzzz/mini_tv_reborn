import time
from screen.st7735 import TFT
from screen.sysfont import sysfont
import random


def show_clock(tft):

    # tft.text((0, 0), str(wifi_handle.ifconfig()), TFT.WHITE, sysfont, 1)
    # time.sleep_ms(5000)
    # tft.fill(TFT.BLACK)

    # v = 30
    # tft.text((0, v), str(1234.567), TFT.BLUE, sysfont, 4, nowrap=True)
    #  tft.text((0, 10), "11:53:24", TFT.GREEN, sysfont, 3, nowrap=True)
    tft.text((0, 10), str(random.random()), TFT.GREEN, sysfont, 3, nowrap=True)
    tft.text((0, 40), "Country", TFT.GREEN, sysfont, 2, nowrap=True)

    # tft.fill(TFT.BLACK)

    # tft.text((0, 10), "09:53:22", TFT.GREEN, sysfont, 3, nowrap=True)
    # tft.text((0, 40), "Mexico", TFT.GREEN, sysfont, 2, nowrap=True)
