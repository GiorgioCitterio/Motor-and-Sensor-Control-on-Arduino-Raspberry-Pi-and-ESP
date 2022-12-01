void setup()
{
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop()
{
  if (Serial.available())
  {
    String str = Serial.readStringUntil('\n');
    if (str.length() > 0)
    {
      int n = str.indexOf(";");
      String rotazione = str.substring(0, n);
      n += 1;
      int vel = str.substring(n, str.length()).toInt();
      if (rotazione == "A")
      {
        digitalWrite(9, LOW);
        digitalWrite(5, HIGH);
        analogWrite(3, vel);
      }

      if (rotazione == "I")
      {
        digitalWrite(9, HIGH);
        digitalWrite(5, LOW);
        analogWrite(3, vel);
      }
    }
  }
}
