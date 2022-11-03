void setup() {
  Serial.begin(1200);
}

void loop() {
  if(Serial.available() > 0) {
    char invio = Serial.read();
    Serial.print(invio);
  }
}
