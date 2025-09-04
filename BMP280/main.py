#Mario UwU 
import board
import busio
import adafruit_bmp280

#con pip install -r requirements.txt se instalan dependencias 
#I2C 0x76 (default del BMP280)

i2c = busio.I2C(board.SCL,board.SDA)
BMP280 = adafruit_bmp280.Adrafruit_BMP280_I2C(i2c)

while True: 
    print(f"Temperatura uwu: {BMP280.temperature:.2f} °C")
    print(f"Presion owo: {BMP280.pressure:.2f} hPa")
    print(f"Altitud: {BMP280.altitude}")
    time.sleep(1)


