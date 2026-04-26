import time
from screen.st7735 import TFT
from screen.sysfont import sysfont


def show_clock(tft, ts_offset=0, subtitle=""):

    ts = time.time() + ts_offset

    current_time = time.localtime(ts)  # get local time tuple

    current_hour = str(current_time[3])
    if len(current_hour) < 2:
        current_hour = "0" + current_hour

    current_minutes = str(current_time[4])
    if len(current_minutes) < 2:
        current_minutes = "0" + current_minutes

    current_seconds = str(current_time[5])
    if len(current_seconds) < 2:
        current_seconds = "0" + current_seconds
    
    current_day = str(current_time[2])
    if len(current_day) < 2:
        current_day = "0" + current_day

    current_month = str(current_time[1])
    if len(current_month) < 2:
        current_month = "0" + current_month
    
    current_year = str(current_time[0])
    if len(current_year) < 2:
        current_year = "0" + current_year

    current_date_to_show = current_day + "-" + current_month + "-" + current_year
    



    # show time on the screen
    tft.text((0, 10),current_hour  + ":" + current_minutes +
             ":" + current_seconds, TFT.GREEN, sysfont, 3, nowrap=True)
    
    tft.text((0, 40), current_date_to_show, TFT.GREEN, sysfont, 2, nowrap=True)
    
    
    tft.text((0, 70), subtitle, TFT.GREEN, sysfont, 2, nowrap=True)

    