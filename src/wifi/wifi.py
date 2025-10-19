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

        time.sleep(0.1)  # Wait 100ms

    # 3. Check and report connection status
    if wlan.isconnected():
        ip_info = wlan.ifconfig()
        # print("\nWi-Fi Connected!")
    else:
        # print("\nWi-Fi Connection Failed.")
        wlan.active(False)  # Turn off the interface

    time.sleep(5)  # short delay to show status

    return wlan
