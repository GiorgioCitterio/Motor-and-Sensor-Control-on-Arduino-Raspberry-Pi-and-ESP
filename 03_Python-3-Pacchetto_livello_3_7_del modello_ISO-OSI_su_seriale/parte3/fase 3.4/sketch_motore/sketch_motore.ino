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
  pinMode(9, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop()
{
  struct pacchettoA1 msg;
  if (Serial.available())
  {
    Serial.readBytes((byte*) &msg, sizeof(msg));
    int controlloId = memcmp(ID, msg.id, 2);
    int controlloDest = memcmp(DESTINATARIO, msg.destinatario, 4);
    int n = sizeof(msg.velocita);
    char vel[4];
    if (controlloId == 0 && controlloDest == 0)
    {
      memcpy(vel,msg.velocita,sizeof(msg.velocita));
      vel[3] = '\0';
      int velocita = atoi(vel);
      String direzione = (String)msg.direzione;
      if (memcmp("A",msg.direzione, 1) == 0)
      {
        digitalWrite(5, LOW);
        digitalWrite(9, HIGH);
        digitalWrite(3, velocita);
      }

      if (memcmp("I",msg.direzione, 1) == 0)
      {
        digitalWrite(5, HIGH);
        digitalWrite(9, LOW);
        digitalWrite(3, velocita);
      }
      if (memcmp("S",msg.direzione, 1) == 0)
      {
        digitalWrite(5, LOW);
        digitalWrite(9, LOW);
        digitalWrite(3, 0);
      }
    }
  }
}
