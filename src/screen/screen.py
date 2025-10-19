from machine import SPI, Pin, I2S
from .st7735 import TFT, TFTColor
from config.config import TFT_PARAMETERS

# ESP32 WROOM D1 MINI ST7735S connections:
"""
Function (Display Pin)	GPIO Number	     Your Code Variable / Pinout:

SCL/SCLK (Clock)	         18	          tft_SCK
SDA / MOSI (Data)	         23	          tft_SDA
CS (Chip Select)	          5	          tft_CS
MISO (Unused by display)	 N/A	      NOT WIRED - But must be defined Pin(19)
DC/A0 (Data/Command)	     17	          tft_A0
RESET	                     16	          tft_RESET
LED/BLK (Backlight)	         22	          Missing in your code - NOT USED

VCC - 3.3V
GND - GND
"""

# Use the correct default GPIO pin numbers for the VSPI (SPI(1)) bus on ESP32
# tft_CS is Chip Select (SS)
# tft_CS = 5
# # tft_SCK is Serial Clock
# tft_SCK = 18
# # tft_SDA is Serial Data/MOSI (Master Out Slave In)
# tft_SDA = 23
# # tft_RESET is Reset
# tft_RESET = 16
# # tft_A0 is Data/Command (DC)
# tft_A0 = 17

# Explicitly define all pins used by the SPI bus and the display
# MISO (GPIO 19) is the default pin for the VSPI bus (SPI(1)).
# Even though the ST7735 doesn't use it, the ESP32 hardware needs it defined
# for proper initialization of the SPI bus.
# spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
#           # <<< MISO fixed here
#           sck=Pin(tft_SCK), mosi=Pin(tft_SDA), miso=Pin(19))


class Screen:

    def __init__(self, channel_id, baudrate, polarity, phase, sck, mosi, miso, a0, reset, cs, rotation=0):
        self.spi = SPI(channel_id, baudrate=baudrate, polarity=polarity,
                       phase=phase, sck=Pin(sck), mosi=Pin(mosi), miso=Pin(miso))

        self.tft = TFT(self.spi, Pin(a0), Pin(reset), Pin(cs))

        self.tft.rotation(rotation)  # 0, 1, 2 or 3

        self.tft.initr()

        self.tft.rgb(True)

    def fill_with_color(self, color):
        """Fill the entire screen with the specified color."""
        self.tft.fill(color)

    def clear(self):
        """Clear the screen (fill with black)."""
        self.tft.fill(TFT.BLACK)

    def show_image(self, image_path, screen_disposition_width, screen_disposition_height):
        """Display a BMP image from the specified path."""
        try:
            with open(image_path, 'rb') as f:
                # Check BMP header
                if f.read(2) == b'BM':
                    dummy = f.read(8)
                    offset = int.from_bytes(f.read(4), 'little')
                    hdrsize = int.from_bytes(f.read(4), 'little')
                    width = int.from_bytes(f.read(4), 'little')
                    height = int.from_bytes(f.read(4), 'little')

                    if int.from_bytes(f.read(2), 'little') == 1:
                        depth = int.from_bytes(f.read(2), 'little')

                        # Check for 24-bit uncompressed format
                        if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:
                            print(f"Loading image: {image_path}")

                            rowsize = (width * 3 + 3) & ~3
                            flip = height >= 0
                            if not flip:
                                height = -height

                            # Constrain to display size (128x160)
                            w, h = min(width, screen_disposition_width), min(
                                height, screen_disposition_height)

                            self.tft._setwindowloc((0, 0), (w - 1, h - 1))

                            for row in range(h):
                                pos = offset + (height - 1 - row) * \
                                    rowsize if flip else offset + row * rowsize
                                f.seek(pos)

                                for col in range(w):
                                    bgr = f.read(3)
                                    self.tft._pushcolor(
                                        TFTColor(bgr[2], bgr[1], bgr[0]))
                        else:
                            print(
                                "Error: Only 24-bit uncompressed BMP is supported.")
                    else:
                        print("Error: Invalid BMP plane count.")
                else:
                    print("Error: File is not a BMP.")

        except Exception as e:
            print(f"Error reading or displaying BMP file: {e}")
            print(f"Ensure '{image_path}' exists on your SD card.")


screen_instance = Screen(
    channel_id=TFT_PARAMETERS["channel_id"],
    baudrate=TFT_PARAMETERS["baudrate"],
    polarity=TFT_PARAMETERS["polarity"],
    phase=TFT_PARAMETERS["phase"],
    sck=TFT_PARAMETERS["sck"],
    mosi=TFT_PARAMETERS["mosi"],
    miso=TFT_PARAMETERS["miso"],
    a0=TFT_PARAMETERS["a0"],
    reset=TFT_PARAMETERS["reset"],
    cs=TFT_PARAMETERS["cs"],
    rotation=TFT_PARAMETERS["rotation"],
)
