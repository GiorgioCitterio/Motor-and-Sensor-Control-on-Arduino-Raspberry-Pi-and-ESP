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
    char c = 0;
    for (int i = 0; i < 8; i++)
    {
      int var = digitalRead(13);
      bitWrite(c, i, var);
      delayMicroseconds(833);
    }
    Serial.print(c);
  }
}
