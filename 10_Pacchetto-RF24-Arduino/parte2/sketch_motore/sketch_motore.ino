#include <RF24.h> 
RF24 radio(7, 8);

#define ID "BE"             
#define TIPO "A1"            
#define DESTINATARIO "A001" 
#define READINGPIPE "00001"    
  
struct pacchettoA1 { 
  char id[2]; 
  char mittente[4]; 
  char destinatario[4]; 
  char tipo[2]; 
  char direzione[1]; 
  char velocita[3]; 
  char vuoto[16]; 
}; 

void setup() {
  Serial.begin(9600); 
  pinMode(9, OUTPUT);
  pinMode(5, OUTPUT);
 
  radio.begin(); 
  radio.setPALevel(RF24_PA_MIN);
  radio.setPayloadSize(32);
  radio.setDataRate(RF24_2MBPS);
  radio.openReadingPipe(0, (byte *) READINGPIPE); 
  radio.startListening();
  if (radio.isChipConnected())
     Serial.println ("nRF24L01p presente");
  else
     Serial.println ("nRF24L01p non rilevato");
}

void loop() {
  struct pacchettoA1 msg;
  if (radio.available())
  {
    radio.read((char*) &msg, sizeof(msg));
    int controlloId = memcmp(ID, msg.id, 2);
    int controlloDest = memcmp(DESTINATARIO, msg.destinatario, 4);
    char vel[4];
    if (controlloId == 0 && controlloDest == 0)
    {
      Serial.println((char *)&msg);
      memcpy(vel,msg.velocita,sizeof(msg.velocita));
      vel[3] = '\0';
      int velocita = atoi(vel);
      if (memcmp("A",msg.direzione, 1) == 0)
      {
        digitalWrite(5, LOW);
        digitalWrite(9, HIGH);
        analogWrite(3, velocita);
      }
      if (memcmp("I",msg.direzione, 1) == 0)
      {
        digitalWrite(5, HIGH);
        digitalWrite(9, LOW);
        analogWrite(3, velocita);
      }
      if (memcmp("S",msg.direzione, 1) == 0)
      {
        digitalWrite(5, LOW);
        digitalWrite(9, LOW);
        analogWrite(3, 0);
      }
    }
  }
}
