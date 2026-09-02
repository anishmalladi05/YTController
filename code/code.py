import time
import board
import digitalio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Initialize BLE and Consumer Control (Media Keys)
ble = BLERadio()
ble.name = "ESP32S3 Media Controller"
hid = HIDService()
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961  # Remote control appearance

cc = ConsumerControl(hid.devices)

# Define button pins (update these to match your XIAO ESP32-S3 pins)
button_pins = (board.D2, board.D3, board.D4, board.D5)
media_codes = (
    ConsumerControlCode.PLAY_PAUSE,
    ConsumerControlCode.VOLUME_INCREMENT,
    ConsumerControlCode.VOLUME_DECREMENT,
    ConsumerControlCode.SCAN_NEXT_TRACK,
]

buttons = []
for pin in button_pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

while True:
    # Advertise if not connected
    if not ble.connected:
        print("Advertising...")
        ble.start_advertising(advertisement)
        while not ble.connected:
            time.sleep(0.1)
        ble.stop_advertising()
        print("Connected!")

    # Check buttons when connected
    while ble.connected:
        for i, btn in enumerate(buttons):
            if not btn.value:  Pressed (LOW with pull-up)
                cc.send(media_codes[i])
                time.sleep(0.3)  # Debounce delay
        time.sleep(0.05)
