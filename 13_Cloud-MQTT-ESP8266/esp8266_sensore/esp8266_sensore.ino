#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

//costanti del sensore
#define ID "BE"
#define TIPO "S1"
#define MITTENTE "M001"
#define DESTINATARIO "P001"
#define VUOTO "----------------"

// WiFi 
const char *WIFI_SSID = "Greppi-2G";  // inserire i dati della rete WiFi 
const char *WIFI_PASSWORD = "withProxy";

// MQTT Broker 
const char *MQTT_BROKER = "172.17.4.29";  // indirizzo IP del broker 
const char *MQTT_USERNAME = ""; // se necessario 
const char *MQTT_PASSWORD = "";
const int MQTT_PORT = 1883;

// topic 
const char *INVIA = "tps/inviaSensore";

//struct sensore
struct pacchettoS1
{
  char id[2];
  char mittente[4];
  char destinatario[4];
  char tipo[2];
  char valoreSensore[4];
  char vuoto[16];
};

// oggetti per wifi e mqtt 
WiFiClient espClient;
PubSubClient client(espClient);

// setup 
void setup()
{
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

  // pubblicazione di un primo messaggio 
  client.publish(INVIA, "Attivo");
}

// ciclo di invio messaggi 
void loop()
{
  StaticJsonDocument<200> doc;
  int num = analogRead(A0); //TODO: pin esp valore potenziometro
  char s[5];
  sprintf(s, "%04d", num);
  struct pacchettoS1 msg;
  memcpy(msg.id, ID, sizeof(msg.id));
  memcpy(msg.mittente, MITTENTE, sizeof(msg.mittente));
  memcpy(msg.destinatario, DESTINATARIO, sizeof(msg.destinatario));
  memcpy(msg.tipo, TIPO, sizeof(msg.tipo));
  memcpy(msg.valoreSensore, s, sizeof(msg.valoreSensore));
  memcpy(msg.vuoto, VUOTO, sizeof(msg.vuoto));
  JsonObject jsonObj = doc.to<JsonObject> ();
  jsonObj["id"] = msg.id;
  jsonObj["mittente"] = msg.mittente;
  jsonObj["destinatario"] = msg.destinatario;
  jsonObj["tipo"] = msg.tipo;
  jsonObj["valoreSensore"] = msg.valoreSensore;
  jsonObj["vuoto"] = msg.vuoto;
  char buffer[200];
  serializeJson(jsonObj, buffer);
  Serial.write(buffer);
  Serial.println();
  client.publish(INVIA, buffer);
  delay(10000);
  client.loop();
}
