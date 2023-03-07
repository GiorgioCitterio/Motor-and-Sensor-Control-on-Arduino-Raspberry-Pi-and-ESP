#include <RF24.h> 
RF24 radio(7, 8);

#define ID "BE"          
#define TIPO "S1"           
#define MITTENTE "M001"    
#define DESTINATARIO "P001" 
#define WRITINGPIPE "00001" 
#define VUOTO "----------------"  

struct pacchettoS1 { 
  char id[2]; 
  char mittente[4]; 
  char destinatario[4]; 
  char tipo[2]; 
  char valoreSensore[4]; 
  char vuoto[16]; 
}; 

void setup() {
  Serial.begin(9600);

  radio.begin(); 
  radio.setPALevel(RF24_PA_MIN); 
  radio.setPayloadSize(32);
  radio.setDataRate(RF24_2MBPS);
  radio.openWritingPipe((byte *)WRITINGPIPE); 
  radio.stopListening();
  if (radio.isChipConnected())
     Serial.println ("nRF24L01p presente");
  else
     Serial.println ("nRF24L01p non rilevato");
}

void loop() {
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
  
  Serial.write((char *)&msg, sizeof(msg));
  Serial.println();

  radio.write((char *)&msg, sizeof(msg)); 

  
  delay(2500);

}
