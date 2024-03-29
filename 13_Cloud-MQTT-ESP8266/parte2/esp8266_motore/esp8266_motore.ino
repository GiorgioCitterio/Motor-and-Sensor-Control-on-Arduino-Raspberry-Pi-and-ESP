#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

#define AVANTI_PIN 12 //D6
#define INDIETRO_PIN 14 //D5
#define VELOCITA_PIN 0 //D3

// WiFi
const char *WIFI_SSID = "Greppi-2G";  // inserire i dati della rete WiFi
const char *WIFI_PASSWORD = "withProxy";

// MQTT Broker
const char *MQTT_BROKER = "172.17.4.29"; // indirizzo IP del broker
const char *MQTT_USERNAME = ""; // se necessario
const char *MQTT_PASSWORD = "";
const int MQTT_PORT = 1883;

// topic
const char *RICEVI = "tps/riceviAttuatore";

// oggetti per wifi e mqtt
WiFiClient espClient;
PubSubClient client(espClient);

// setup
void setup()
{
  pinMode(AVANTI_PIN, OUTPUT);
  pinMode(INDIETRO_PIN, OUTPUT);
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

void loop()
{
  client.loop();
}

// funzione di callback
void callback(char *topic, byte *payload, unsigned int length)
{
  StaticJsonDocument<200> jsonDoc;
  Serial.print("Arrivato un messaggio nel topic: ");
  Serial.println(topic);
  Serial.println("Messaggio:");
  for (int i = 0; i < length; i++)
  {
    Serial.print((char) payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");

  deserializeJson(jsonDoc, payload, length);
  const char* direzione = jsonDoc["direzione"];
  int velocita = jsonDoc["velocita"];
  Serial.println(velocita);
  Serial.println(direzione);
  if (strcmp("A", direzione) == 0)
  {
    digitalWrite(INDIETRO_PIN, LOW);
    digitalWrite(AVANTI_PIN, HIGH);
    analogWrite(VELOCITA_PIN, velocita);
  }
  if (strcmp("I", direzione) == 0)
  {
    digitalWrite(INDIETRO_PIN, HIGH);
    digitalWrite(AVANTI_PIN, LOW);
    analogWrite(VELOCITA_PIN, velocita);
  }
}
