import asyncio 
from bleak import BleakClient 
import time 

#58:BF:25:9D:E9:B6
ESP32_ADDRESS = "C8:C9:A3:CB:F5:66" 
CHARACTERISTIC_UUID2 = "22222222-36e1-4688-b7f5-ea07361b26a8" 
 
async def main(address,uuid): 
    async with BleakClient(address) as client: 
        while True: 
            value = await client.read_gatt_char(uuid) 
            print(value) 
            time.sleep(5) 
 
asyncio.run(main(ESP32_ADDRESS,CHARACTERISTIC_UUID2)) 