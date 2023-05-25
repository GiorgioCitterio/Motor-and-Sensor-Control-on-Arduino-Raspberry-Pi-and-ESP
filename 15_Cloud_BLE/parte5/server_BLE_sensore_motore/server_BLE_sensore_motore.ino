#include <BLEDevice.h> 
#include <BLEUtils.h> 
#include <BLEServer.h> 
 
// definizione degli UID del servizio e delle due caratteristiche 
#define SERVICE_UUID         "177c5272-c6c8-4ecd-a2e4-6e6bb7651ce1" 
#define CHARACTERISTIC_UUID1 "776be67f-9fcb-40b7-87cb-458e23f15638"  
#define CHARACTERISTIC_SENSOR "a89adab3-fb71-488d-940f-dea867890df9"
#define CHARACTERISTIC_MOTORDIRECTION "a395aaa4-12fd-484f-b2e7-b4941e0e001a"
#define CHARACTERISTIC_MOTORSPEED "8f0a2fa8-cad4-435d-907b-38f44f4fe5d3"
#define ADCPIN A0 //SP
#define AVANTI_PIN 12 //D6
#define INDIETRO_PIN 14 //D5
#define VELOCITA_PIN 0 //D3
 
BLEServer *pServer; 
BLEService *pService; 
BLECharacteristic *pCharacteristic1;
BLECharacteristic *pCharacteristicSensor; 
BLECharacteristic *pCharacteristicMotorDirection; 
BLECharacteristic *pCharacteristicMotorSpeed; 
 
 
void setup() 
{
  Serial.begin(115200); 
  Serial.println("Starting BLE Server!"); 
 
  // attivazione del device BLE e creazione delle caratteristiche 
  // la prima in R/W la seconda solo R 
  BLEDevice::init("Controllo ambiente gioUmbe"); 
  pServer = BLEDevice::createServer(); 
  pService = pServer->createService(SERVICE_UUID); 
  pCharacteristic1 = pService->createCharacteristic( 
                       CHARACTERISTIC_UUID1, 
                       BLECharacteristic::PROPERTY_READ | 
                       BLECharacteristic::PROPERTY_WRITE);
  pCharacteristicSensor = pService->createCharacteristic( 
                       CHARACTERISTIC_SENSOR, 
                       BLECharacteristic::PROPERTY_READ); 
  pCharacteristicMotorDirection = pService->createCharacteristic( 
                       CHARACTERISTIC_MOTORDIRECTION, 
                       BLECharacteristic::PROPERTY_WRITE);
  pCharacteristicMotorSpeed = pService->createCharacteristic( 
                       CHARACTERISTIC_MOTORSPEED, 
                       BLECharacteristic::PROPERTY_WRITE);                 
                       
  // impostazione dei valori iniziali delle caratteristiche 
  pCharacteristic1->setValue("init"); 
  pCharacteristicSensor->setValue("0");
  pCharacteristicMotorDirection->setValue("A");
  pCharacteristicMotorSpeed->setValue("0");
 
  // attivazione del servizio e del'advertising 
  pService->start(); 
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising(); 
  pAdvertising->addServiceUUID(SERVICE_UUID); 
  pAdvertising->setScanResponse(true); 
  pAdvertising->setMinPreferred(0x12); 
  BLEDevice::startAdvertising(); 
} 

void loop() 
{
  // acquisizione del valore della prima caratteristica 
  std::string value = pCharacteristic1->getValue(); 

  //lettura valori sensore e salvataggio
  int num = analogRead(ADCPIN);
  char s[5];
  sprintf(s, "%04d", num);
  pCharacteristicSensor -> setValue(s);

  //controllo del motore 
  std::string velocita = pCharacteristicMotorSpeed->getValue();
  std::string direzione = pCharacteristicMotorDirection->getValue();
 
  // stampa 
  Serial.print("Caratteristica 1: "); 
  Serial.print(value.c_str());
  Serial.print("    -    Caratteristica sensore: ");
  Serial.print(s);
  Serial.println();
  Serial.print("Caratteristica motore direzione: "); 
  Serial.print(direzione.c_str());
  Serial.print("    -    Caratteristica motore velocità: "); 
  Serial.print(velocita.c_str());
  Serial.println();
 
  // ripresa dell'advertising 
  BLEDevice::startAdvertising(); 
 
  delay(2000); 
}
