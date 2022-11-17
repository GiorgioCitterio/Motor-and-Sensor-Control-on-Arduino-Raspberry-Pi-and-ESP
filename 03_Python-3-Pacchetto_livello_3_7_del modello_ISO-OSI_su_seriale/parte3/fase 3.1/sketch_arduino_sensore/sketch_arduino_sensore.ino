#define ID "BE"
#define MITTENTE "M001"
#define DESTINATARIO "D031"
#define TIPO "S1"
#define VUOTO "----------------"

struct pacchettoS1 {
    char id[2];
    char mittente[4];
    char destinatario[4];
    char tipo[2];
    char valoreSensore[4];
    char vuoto[16];
  };

void setup()
{
  Serial.begin(9600);
}
void loop()
{  
  int num = analogRead(A0);
  char s[5];
  sprintf(s, "%04d", num);
  
  struct pacchettoS1 msg;
  memcpy(msg.id, ID, sizeof(msg.id));
  memcpy(msg.mittente, MITTENTE, sizeof(msg.mittente));
  memcpy(msg.destinatario, DESTINATARIO, sizeof(msg.destinatario));
  memcpy(msg.tipo, TIPO, sizeof(msg.tipo));
  memcpy(msg.valoreSensore, s, sizeof(msg.valoreSensore));
  memcpy(msg.vuoto, VUOTO, sizeof(msg.vuoto));
  
  Serial.write((byte *)&msg, sizeof(msg));
  
  delay(1000);
}
