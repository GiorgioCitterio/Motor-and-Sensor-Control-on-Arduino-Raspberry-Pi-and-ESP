String direzione;
int velocita;

void setup()
{
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {
    String point = Serial.readStringUntil('\n');
    if (point.length() > 0)
    {
      int x = 0;
      int y = point.indexOf(";");
      int z = 0;
      while (y > 0)
      {
        String num = point.substring(y, x);
        x = y + 1;
        y = point.indexOf(";", y + 1);

        processnum(z, num);
        z++;
      }

      if (direzione == "avanti")
      {
        digitalWrite(7, HIGH);
        digitalWrite(8, LOW);
        analogWrite(6, velocita);
        Serial.println("ON");
      }

      if (direzione == "indietro")
      {
        digitalWrite(7, LOW);
        digitalWrite(8, HIGH);
        analogWrite(6, velocita);
        Serial.println("OFF");
      }
    }
  }
}
