char array[20];
void setup()
{
  Serial.begin(1200);
  pinMode(13, INPUT);
}

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
  }
}
