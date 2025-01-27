import time  # Required for sleep functionality

desiredHumidity = 55

def sleep(seconds):
    time.sleep(seconds)  # Pauses execution for the specified time

def lowEnergyMode():
    print("Low Fan Speed")
    sleep(2)

def highEnergyMode():
    print("High Fan Speed")
    sleep(2)

def sleepForNow():
    print("Powering off for now")
    sleep(4)

sensorValues = [76, 66, 54, 53, 80, 76, 20, 500, 56, 70]

def selectCorrectMode(measuredHumidity):
    # Checks if the humidity deviation requires high energy mode
    if measuredHumidity - desiredHumidity >= 10:
        print("Humidity Sensor Value:", measuredHumidity)
        highEnergyMode()
    else:
        # Runs low energy mode for smaller deviations
        print("Humidity Sensor Value:", measuredHumidity)
        lowEnergyMode()

# Loops through the sensor values to determine the dehumidifier's action
for measuredHumidity in sensorValues:
    if measuredHumidity != desiredHumidity:
        selectCorrectMode(measuredHumidity)
    else:
        print("Good Humidity, Powering Off For Now")
        sleepForNow()
