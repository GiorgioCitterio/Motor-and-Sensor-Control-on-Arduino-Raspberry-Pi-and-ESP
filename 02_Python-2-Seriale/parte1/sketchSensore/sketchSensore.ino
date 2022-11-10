void setup()
{
  Serial.begin(9600);
}
void loop()
{
  int num = analogRead(A0);
  Serial.println(num);
  delay(1000);
}
