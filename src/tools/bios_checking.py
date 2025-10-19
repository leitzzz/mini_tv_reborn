from screen.st7735 import TFT
from screen.sysfont import sysfont


def bios_check(board_info, tft):
    """Display Hardware information in the screen."""
    tft.text((0, 10),
             "BOARD CHECK:", TFT.WHITE, sysfont, 2, nowrap=True)

    bios_info_counter = 3  # start from line 30, and helps to manage line spacing
    for key, value in board_info.items():
        tft.text((0, 10 * bios_info_counter),
                 f"{key}: {value}", TFT.WHITE, sysfont, 1, nowrap=True)

        bios_info_counter += 1
