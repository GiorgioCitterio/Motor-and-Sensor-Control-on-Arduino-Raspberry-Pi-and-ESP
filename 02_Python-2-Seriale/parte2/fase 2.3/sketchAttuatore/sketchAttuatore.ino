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
      Serial.println(rotazione);
      n += 1;
      int vel = str.substring(n, str.length()).toInt();
      Serial.println(vel);
      if (rotazione == "avanti")
      {
        digitalWrite(3, LOW);
        digitalWrite(5, HIGH);
        digitalWrite(9, vel);
        Serial.println("avanti");
      }

      if (rotazione == "indietro")
      {
        digitalWrite(3, HIGH);
        digitalWrite(5, LOW);
        digitalWrite(9, vel);
        Serial.println("indietro");
      }
      if (rotazione == "stop")
      {
        digitalWrite(3, LOW);
        digitalWrite(5, LOW);
        digitalWrite(9, 0);
        Serial.println("spento");
      }
    }
  }
}
