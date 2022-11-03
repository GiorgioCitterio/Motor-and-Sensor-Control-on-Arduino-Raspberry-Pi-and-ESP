void setup() {
  Serial.begin(1200);
  pinMode(13, INPUT);
}

void loop() {
  char carattereRicevuto = digitalRead(13);
  Serial.print(carattereRicevuto); 
}
