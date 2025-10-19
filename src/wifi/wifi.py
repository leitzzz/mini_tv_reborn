import time
import network


def connect_wifi(ssid, password):
    """Connects the board to the specified Wi-Fi network."""

    # 1. Initialize the Wi-Fi interface in Station mode
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Check if already connected
    if wlan.isconnected():
        # print("Already connected to Wi-Fi.")
        return wlan

    # print(f"Connecting to Wi-Fi network: {ssid}...")

    # 2. Start the connection process
    wlan.connect(ssid, password)

    # Simple connection attempt loop (waits up to 10 seconds)
    max_wait = 100  # 100 * 100ms = 10 seconds
    while max_wait > 0:
        if wlan.isconnected():
            break
        max_wait -= 1
        # print('.', end='')
        # Optional visual feedback on screen
        # tft.text((0, 70), '.', TFT.YELLOW, sysfont, 2, nowrap=True)
        time.sleep(0.1)  # Wait 100ms

    # 3. Check and report connection status
    if wlan.isconnected():
        ip_info = wlan.ifconfig()
        # print("\nWi-Fi Connected!")
        # print(f"IP Address: {ip_info[0]}")
        # tft.text((0, 10), "Connected!",
        #          TFT.GREEN, sysfont, 2, nowrap=True)
        # tft.text((0, 40), f"Local IP: {ip_info[0]}",
        #          TFT.GREEN, sysfont, 1, nowrap=True)
    else:
        # print("\nWi-Fi Connection Failed.")
        # tft.text((0, 20), "WIFI Connection Failed!",
        #          TFT.RED, sysfont, 1, nowrap=True)
        wlan.active(False)  # Turn off the interface

    time.sleep(5)  # short delay to show status

    return wlan
