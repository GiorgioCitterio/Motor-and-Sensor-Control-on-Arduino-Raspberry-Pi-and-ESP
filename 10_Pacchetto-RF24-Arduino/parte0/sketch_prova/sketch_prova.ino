#include <RF24.h>
RF24 radio(7, 8); // Imposta CE e nCSN conformemente all'hardware

void setup() {
  Serial.begin(9600);
  radio.begin();
}

void loop() {
  if (radio.isChipConnected())
     Serial.println ("nRF24L01p presente");
  else
     Serial.println ("nRF24L01p non rilevato");
  delay(1000);
}
