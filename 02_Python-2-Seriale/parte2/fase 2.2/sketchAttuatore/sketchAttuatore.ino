char comando;
int velocita = 500;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  comando = Serial.read();
  if (comando == 'a') {
    digitalWrite(7, 1);
    digitalWrite(8, 0);
    analogWrite(6, velocita);
    Serial.println("ON");
  }
  if (comando == 's') {
     digitalWrite(7, 0);
     digitalWrite(8, 1);
     analogWrite(6, 0);
     Serial.println("OFF");
  }
}
