#define ID "BE"
#define DESTINATARIO "D031"

struct pacchettoA1
{
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
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop()
{
  char vel[4];
  struct pacchettoA1 msg;
  if (Serial.available())
  {
    Serial.readBytes((byte*) &msg, sizeof(msg));
    int controlloId = memcmp(ID, msg.id, 2);
    int controlloDest = memcmp(DESTINATARIO, msg.destinatario, 4);
    if (controlloId == 0 && controlloDest == 0)
    {
      strcpy(vel, msg.velocita);
      int velocita = atoi(vel);
      String direzione = (String)msg.direzione;
      if (direzione == "a")
      {
        digitalWrite(3, LOW);
        digitalWrite(5, HIGH);
        digitalWrite(9, velocita);
      }

      if (direzione == "i")
      {
        digitalWrite(3, HIGH);
        digitalWrite(5, LOW);
        digitalWrite(9, velocita);
      }
    }
  }
}
