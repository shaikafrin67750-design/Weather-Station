# Weather Station using Python

import random
import time

def weather_station():
# Simulate sensor readings
temperature = random.uniform(20, 40)
humidity = random.uniform(30, 90)
pressure = random.uniform(990, 1030)
wind_speed = random.uniform(0, 30)

```
print("\n===== WEATHER STATION =====")
print(f"Temperature : {temperature:.2f} °C")
print(f"Humidity    : {humidity:.2f} %")
print(f"Pressure    : {pressure:.2f} hPa")
print(f"Wind Speed  : {wind_speed:.2f} km/h")

if temperature > 35:
    print("Temperature Status: HOT")
elif temperature < 25:
    print("Temperature Status: COOL")
else:
    print("Temperature Status: NORMAL")

if humidity > 70:
    print("Humidity Status: HIGH")
elif humidity < 40:
    print("Humidity Status: LOW")
else:
    print("Humidity Status: NORMAL")
```

print("Weather Station Started")
print("Press Ctrl+C to stop.")

try:
while True:
weather_station()
time.sleep(5)

except KeyboardInterrupt:
print("\nWeather Station Closed.")
