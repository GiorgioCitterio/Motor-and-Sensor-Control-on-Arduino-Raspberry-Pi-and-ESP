char array[20];
void setup()
{
  Serial.begin(1200);
  pinMode(13, INPUT);
}

void loop()
{
  while(Serial.available() == false){
    delayMicroseconds((1/1200)*1.5);
    Serial.readBytes(array, 13);
    Serial.write(array);
  }
}
