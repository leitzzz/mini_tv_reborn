# this file serves as a sample configuration file.
# rename it to config.py and edit the parameters as needed.

# WiFi configuration parameters
WIFI_PARAMETERS = {
    "ssid": "YOUR_SSID_HERE",
    "password": "YOUR_PASSWORD_HERE"
}

# TFT (screen) configuration parameters
TFT_PARAMETERS = {
    "channel_id": 1,  # SPI channel -> example SPI(1,....) on ESP32
    "baudrate": 20000000,
    "polarity": 0,
    "phase": 0,
    "sck": 18,
    "mosi": 23,  # sda
    "miso": 19,
    "cs": 5,
    "reset": 16,
    "a0": 17,
    "rotation": 3,
    # X pixels width on the disposition based on the "rotation" key
    "screen_disposition_width": 160,
    # Y pixels height on the disposition based on the "rotation" key
    "screen_disposition_height": 128,
}

# Available .wav files in assets/audio/:
WAV_AUDIOS = {
    "ding": "assets/audio/ding.wav",
    "chimes": "assets/audio/chimes.wav",
    "notify": "assets/audio/notify.wav",
    "chord": "assets/audio/chord.wav",
    "ringin": "assets/audio/ringin.wav",
    "ringout": "assets/audio/ringout.wav",
    "tada": "assets/audio/tada.wav",
    "bios_beep": "assets/audio/bios.wav",
    "error": "assets/audio/error.wav",
}

# available board and hardware information.
BIOS_INFO = {
    "Board": "ESP Wroom 32 D1 Mini",
    "Dual-core": "32bit LX6 240MHz",
    "SRAM": "520KB",
    "ROM": "448KB",
    "Flash Mem": "4MB",
    "Case": "Casio TV-800",
    "Sound": "I2S MAX98357A",
    "Scr": "ST7735S 1.8in 160x128",
}

GENERAL_CONFIG = {
    # seconds, if is set to 0 no reboot will perform
    "reboot_after_no_wifi_connection": 0,
}
