void setup() {
  Serial.begin(1200);
  pinMode(13, INPUT_PULLUP);
}

void loop() {
  while(true) {
    if(digitalRead(13) == HIGH) {
      char var = analogRead(13); 
      Serial.print(var); 
    } 
    delay(500);
  }
}
