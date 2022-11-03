void setup() {
  Serial.begin(1200);
}

void loop() {
  char var = Serial.read();
  Serial.print(var);
  delay(500); 
}
