#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//costanti del motore
#define ID "BE"
#define TIPO "A1"
#define DESTINATARIO "A001"

// WiFi
const char *WIFI_SSID = "Greppi-2G";  // inserire i dati della rete WiFi
const char *WIFI_PASSWORD = "withProxy";

// MQTT Broker
const char *MQTT_BROKER = "172.17.4.29";  // indirizzo IP del broker
const char *MQTT_USERNAME = ""; // se necessario
const char *MQTT_PASSWORD = "";
const int MQTT_PORT = 1883;

// topic
const char *RICEVI = "tps/riceviAttuatore";

//struct motore
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

// oggetti per wifi e mqtt
WiFiClient espClient;
PubSubClient client(espClient);

// setup
void setup()
{
  pinMode(8, OUTPUT);
  pinMode(5, OUTPUT);
  Serial.begin(111520);
  Serial.println("Inizio");
  Serial.print("Connessione al WiFi..");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("Connesso");

  // assegna un nome questo client
  String client_id = "esp8266-client-gioUmbe" + String(WiFi.macAddress());
  Serial.printf("%s in connessione al MQTT ..", client_id.c_str());
  client.setServer(MQTT_BROKER, MQTT_PORT);
  client.setCallback(callback);
  while (!client.connected())
  {
    if (client.connect(client_id.c_str(), MQTT_USERNAME, MQTT_PASSWORD))
    {
      Serial.println("Connesso al broker mqtt");
    }
    else
    {
      Serial.print("Fallito con codice di errore: ");
      Serial.println(client.state());
      Serial.println("Ritento");
      delay(2000);
    }
  }

  //sottoscrizione  
  client.subscribe(RICEVI);
}

void loop() {}

// funzione di callback 
void callback(char *topic, byte *payload, unsigned int length)
{
  Serial.print("Arrivato un messaggio nel topic: ");
  Serial.println(topic);
  Serial.print("Messaggio:");
  for (int i = 0; i < length; i++)
  {
    Serial.print((char) payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
  struct pacchettoA1 msg;
  
  memcpy(msg.id, payload, 2);
  memcpy(msg.mittente, payload + 2, 4);
  memcpy(msg.destinatario, payload + 6, 4);
  memcpy(msg.tipo, payload + 10, 2);
  memcpy(msg.direzione, payload + 12, 1);
  memcpy(msg.velocita, payload + 13, 3);
  memcpy(msg.vuoto, payload + 16, 16);

  int controlloId = memcmp(ID, msg.id, 2);
  int controlloDest = memcmp(DESTINATARIO, msg.destinatario, 4);
  char vel[4];
  if (controlloId == 0 && controlloDest == 0)
  {
    Serial.println((char*) &msg);
    memcpy(vel, msg.velocita, sizeof(msg.velocita));
    vel[3] = '\0';
    int velocita = atoi(vel);
    if (memcmp("A", msg.direzione, 1) == 0)
    {
      digitalWrite(5, LOW);
      digitalWrite(8, HIGH);
      analogWrite(3, velocita);
    }
    if (memcmp("I", msg.direzione, 1) == 0)
    {
      digitalWrite(5, HIGH);
      digitalWrite(8, LOW);
      analogWrite(3, velocita);
    }
  }
}
