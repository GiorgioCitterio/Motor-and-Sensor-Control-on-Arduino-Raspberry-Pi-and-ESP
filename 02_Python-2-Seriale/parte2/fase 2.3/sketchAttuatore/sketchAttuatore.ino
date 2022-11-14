void setup()
{
  Serial.begin(9600);
  pinMode(3, OUTPUT);
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
      if (rotazione == "avanti")
      {
        digitalWrite(3, HIGH);
        digitalWrite(5, LOW);
        analogWrite(9, vel);
      }

      if (rotazione == "indietro")
      {
        digitalWrite(3, LOW);
        digitalWrite(5, HIGH);
        analogWrite(9, vel);
      }
    }
  }
}
