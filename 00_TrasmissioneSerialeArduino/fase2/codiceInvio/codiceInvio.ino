void setup() {
  Serial.begin(1200);
}

void loop() {
<<<<<<< HEAD
  char var = Serial.read();
  Serial.print(var);
  delay(500); 
=======
  if(Serial.available() > 0) {
    char invio = Serial.read();
    Serial.print(invio);
  }
>>>>>>> 694605e01f1a8c9290c80d59f4e48902e06c4270
}
