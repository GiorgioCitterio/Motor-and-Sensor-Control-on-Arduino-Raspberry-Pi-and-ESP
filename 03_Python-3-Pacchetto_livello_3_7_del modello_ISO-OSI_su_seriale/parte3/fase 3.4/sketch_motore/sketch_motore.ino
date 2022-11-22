#define ID "BE"
#define DESTINATARIO "D031"

struct pacchettoA1 {
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char direzione[1];
  char velocita[3];
  char vuoto[16];
};

void setup()
{
  Serial.begin(9600);
}
void loop()
{  
  if (Serial.available()){
    int msg = Serial.readBytes((byte *) &msg, sizeof(msg));
  }
}
