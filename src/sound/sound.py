from screen.st7735 import TFT
from screen.sysfont import sysfont

from machine import Pin, I2S

# --- File and Audio Configuration ---
# REPLACE with the actual filename of your WAV file (must be 16-bit PCM)
# converted previously to 44100 Hz, 16-bit, Stereo with ffmpeg
# example: ffmpeg -i TADA.WAV -ac 1 -ar 44100 -acodec pcm_s16le tada_1.wav

# WAV_FILENAME = "../assets/audio/ding.wav"
# Make sure this matches the actual properties of your audio file
SAMPLE_RATE = 44100
BITS = 16
CHANNELS = I2S.STEREO

# WAV file header size (to skip past metadata)
WAV_HEADER_SIZE = 44

# ------------------------------------

# -------------------------------------------------------------
# MAX98357A I2S Setup
# -------------------------------------------------------------

I2S_ID = 0
I2S_BCLK = 25       # Bit Clock (BCLK)
I2S_WCLK = 26       # Word Clock / LRC
I2S_DOUT = 27       # Data Out / DIN


class Sound():
    def __init__(self):
        self.audio_out = I2S(
            I2S_ID,
            sck=Pin(I2S_BCLK),
            ws=Pin(I2S_WCLK),
            sd=Pin(I2S_DOUT),
            mode=I2S.TX,
            bits=BITS,
            format=CHANNELS,
            rate=SAMPLE_RATE,
            ibuf=4096,  # Internal buffer size
        )

    def play_sound(self, filename, tft):
        """Reads a WAV file from the internal filesystem and streams it to I2S."""

        # print(f"Attempting to play local file: {filename}")
        # tft.text((0, 110), f"Playing: {filename}",
        #          TFT.CYAN, sysfont, 1, nowrap=True)

        try:
            # Open the WAV file in binary read mode
            with open(filename, 'rb') as audio_file:
                # 1. Skip the WAV header (44 bytes)
                header_data = audio_file.read(WAV_HEADER_SIZE)
                if len(header_data) != WAV_HEADER_SIZE:
                    raise Exception("File too short or corrupted.")

                # print(f"Skipped {len(header_data)} bytes (WAV Header).")
                # tft.text((0, 130), "Skipped Header. Playing...",
                #          TFT.GREEN, sysfont, 1, nowrap=True)

                # 2. Stream the rest of the data to I2S
                audio_buffer = bytearray(1024)
                bytes_read_total = 0

                # print("Starting audio playback...")
                while True:
                    # Read a chunk of raw audio data from the file
                    bytes_read = audio_file.readinto(audio_buffer)

                    if bytes_read is None or bytes_read == 0:
                        # End of file
                        break

                    # Write the data chunk to the I2S peripheral
                    # Note: audio_out.write returns the number of bytes written
                    self.audio_out.write(audio_buffer[:bytes_read])
                    bytes_read_total += bytes_read

            # print(
            #     f"Playback finished. Total audio bytes streamed: {bytes_read_total}")
            # tft.text((0, 150), "Playback Finished.",
            #         TFT.YELLOW, sysfont, 1, nowrap=True)

        except OSError as e:
            # print(f"Error opening/reading file: {e}")
            tft.text((0, 130), f"File Error: {e}",
                     TFT.RED, sysfont, 1, nowrap=True)

        except Exception as e:
            # print(f"An unexpected error occurred: {e}")
            tft.text((0, 130), f"Play Error: {e}",
                     TFT.RED, sysfont, 1, nowrap=True)

    def deinit_audio(self):
        """De-initialize the I2S peripheral."""
        if self.audio_out:
            self.audio_out.deinit()


sound = Sound()
