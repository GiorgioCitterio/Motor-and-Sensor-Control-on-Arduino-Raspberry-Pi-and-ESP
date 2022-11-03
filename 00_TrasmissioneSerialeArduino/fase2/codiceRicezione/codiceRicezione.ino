void setup()
{
  Serial.begin(1200);
  pinMode(13, INPUT);
}

void loop()
{
  if (digitalRead(13) == LOW)
  {
    delayMicroseconds(1250);
    for (int i = 0; i < 8; i++)
    {
      char var = digitalRead(13);
      Serial.print(var);
      delay(1/1200);
    }
  }
}
