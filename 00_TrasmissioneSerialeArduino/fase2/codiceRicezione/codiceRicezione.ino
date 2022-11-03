char array[20];
void setup()
{
  Serial.begin(1200);
  pinMode(13, INPUT_PULLUP);
}

<<<<<<< HEAD
void loop()
{
  if (analogRead(13) == LOW)
  {
    delayMicroseconds(1250);
    for (int i = 0; i < 8; i++)
    {
      char var = analogRead(13);
      Serial.print(var);
      delayMicroseconds(1250);
    }
=======
void loop() {
  while(true) {
    if(digitalRead(13) == HIGH) {
      char var = analogRead(13); 
      Serial.print(var); 
    } 
    delay(500);
>>>>>>> 694605e01f1a8c9290c80d59f4e48902e06c4270
  }
}
