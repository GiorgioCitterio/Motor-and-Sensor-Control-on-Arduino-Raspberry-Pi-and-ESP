#include <BLEDevice.h> 
#include <BLEUtils.h> 
#include <BLEServer.h> 
 
// definizione degli UID del servizio e delle due caratteristiche 
#define SERVICE_UUID         "00000000-1fb5-459e-8fcc-c5c9c331914b" 
#define CHARACTERISTIC_UUID1 "11111111-36e1-4688-b7f5-ea07361b26a8" 
#define CHARACTERISTIC_UUID2 "22222222-36e1-4688-b7f5-ea07361b26a8" 
#define CHARACTERISTIC_SENSOR "33333333-36e1-4688-b7f5-ea07361b26a8"
#define ADCPIN A0
 
BLEServer *pServer; 
BLEService *pService; 
BLECharacteristic *pCharacteristic1; 
BLECharacteristic *pCharacteristic2; 
BLECharacteristic *pCharacteristicSensor; 
 
 
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
  pCharacteristic2 = pService->createCharacteristic( 
                       CHARACTERISTIC_UUID2, 
                       BLECharacteristic::PROPERTY_READ); 
  pCharacteristicSensor = pService->createCharacteristic( 
                       CHARACTERISTIC_SENSOR, 
                       BLECharacteristic::PROPERTY_READ);                  
                       
  // impostazione dei valori iniziali delle caratteristiche 
  pCharacteristic1->setValue("init"); 
  pCharacteristic2->setValue("1");
  pCharacteristicSensor->setValue("0");
 
  // attivazione del servizio e del'advertising 
  pService->start(); 
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising(); 
  pAdvertising->addServiceUUID(SERVICE_UUID); 
  pAdvertising->setScanResponse(true); 
  pAdvertising->setMinPreferred(0x12); 
  BLEDevice::startAdvertising(); 
} 
int i = 0; 
void loop() 
{
  int num = analogRead(ADCPIN);
  char s[5];
  sprintf(s, "%04d", num);
  pCharacteristicSensor -> setValue(s);
  
  // acquisizione del valore della prima caratteristica 
  std::string value = pCharacteristic1->getValue(); 
 
  // impostazione del valore della seconda caratteristica 
  // (valore progressivo)
  char str[100]; 
  sprintf(str, "%d", i++); 
  pCharacteristic2->setValue(str); 
 
  // stampa 
  Serial.print("Caratteristica sensore: ");
  Serial.print(s);
  Serial.print("    -    Caratteristica 1: "); 
  Serial.print(value.c_str()); 
  Serial.print("    -    Caratteristica 2: "); 
  Serial.println(i);
 
  // ripresa dell'advertising 
  BLEDevice::startAdvertising(); 
 
  delay(2000); 
}
