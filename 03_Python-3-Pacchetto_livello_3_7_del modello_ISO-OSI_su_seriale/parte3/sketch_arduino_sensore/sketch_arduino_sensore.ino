#define ID "BE"
#define MITTENTE "M001"
#define DESTINATARIO "D031"

struct pacchettoS1 {
    char id[2];
    char mittente[4];
    char destinatario[4];
    char tipo[2];
    char valoreSensore[4];
    char vuoto[16]
  };

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  
  struct pacchettoS1 msg;
  memcpy(msg.id, ID, sizeof(msg.id);
  int num = analogRead(A0);
  char s[5];
  sprintf(s, "%04d", num);
  Serial.write((byte *)&msg, sizeof(msg));
  delay(1000);
  if (Serial.available())
  {
    
  }
  }
}
