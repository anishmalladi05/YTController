#include <BleKeyboard.h>

// Initialize the Bluetooth Keyboard object with Name, Manufacturer, and Initial Battery Level
BleKeyboard bleKeyboard("ESP32 Media Controller", "DIY", 100);

// Define your button pins (assuming buttons connect pin to GND)
const int BUTTON_PLAY_PAUSE = 2;
const int BUTTON_VOL_UP     = 3;
const int BUTTON_VOL_DOWN   = 4;
const int BUTTON_NEXT       = 5;

void setup() {
  Serial.begin(115200);
  
  // Configure button pins as inputs with internal pull-ups
  pinMode(BUTTON_PLAY_PAUSE, INPUT_PULLUP);
  pinMode(BUTTON_VOL_UP,     INPUT_PULLUP);
  pinMode(BUTTON_VOL_DOWN,   INPUT_PULLUP);
  pinMode(BUTTON_NEXT,       INPUT_PULLUP);

  // Start the BLE keyboard service
  bleKeyboard.begin();
}

void loop() {
  // Only process button inputs if a device is connected via Bluetooth
  if (bleKeyboard.isConnected()) {

    // Play / Pause Button
    if (digitalRead(BUTTON_PLAY_PAUSE) == LOW) {
      bleKeyboard.write(KEY_MEDIA_PLAY_PAUSE);
      delay(300); // Debounce delay
    }

    // Volume Up Button
    if (digitalRead(BUTTON_VOL_UP) == LOW) {
      bleKeyboard.write(KEY_MEDIA_VOLUME_UP);
      delay(150); // Shorter delay for quick volume adjustments
    }

    // Volume Down Button
    if (digitalRead(BUTTON_VOL_DOWN) == LOW) {
      bleKeyboard.write(KEY_MEDIA_VOLUME_DOWN);
      delay(150);
    }

    // Next Track Button
    if (digitalRead(BUTTON_NEXT) == LOW) {
      bleKeyboard.write(KEY_MEDIA_NEXT_TRACK);
      delay(300);
    }
  }
  
  // Small loop delay to save power and stabilize reading
  delay(20);
}
