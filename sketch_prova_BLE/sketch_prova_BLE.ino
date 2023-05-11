#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>
// definizione degli UID del servizio edelle due caratteristiche
#define SERVICE_UUID         "00000000-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID1 "11111111-36e1-4688-b7f5-ea07361b26a8"
#define CHARACTERISTIC_UUID2 "22222222-36e1-4688-b7f5-ea07361b26a8"
BLEServer *pServer;
BLEService *pService;
BLECharacteristic *pCharacteristic1;
BLECharacteristic *pCharacteristic2;
void setup()
{
  Serial.begin(9600);
  Serial.println("Starting BLE Server!");
  // attivazione del device BLE e creazione delle caratteristiche
  // la prima inR/W la seconda solo R
  BLEDevice::init("Emilio");
  pServer = BLEDevice::createServer();
  pService = pServer->createService(SERVICE_UUID);
  pCharacteristic1 = pService->createCharacteristic(
    CHARACTERISTIC_UUID1,
    BLECharacteristic::PROPERTY_READ |
    BLECharacteristic::PROPERTY_WRITE);
  pCharacteristic2 = pService->createCharacteristic(
    CHARACTERISTIC_UUID2,
    BLECharacteristic::PROPERTY_READ);
}
