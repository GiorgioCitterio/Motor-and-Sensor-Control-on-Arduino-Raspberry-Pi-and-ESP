void setup()
{
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
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
      n += 2;
      int vel = str.substring(n, str.length());
      if (rotazione == "avanti")
      {
        digitalWrite(7, HIGH);
        digitalWrite(8, LOW);
        analogWrite(9, vel);
      }

      if (rotazione == "indietro")
      {
        digitalWrite(7, LOW);
        digitalWrite(8, HIGH);
        analogWrite(9, vel);
      }
    }
  }
}
