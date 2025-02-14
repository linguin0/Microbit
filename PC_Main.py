import serial

connection = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)

print("Waiting...")
file = open("data.csv", "w")

loop = True
while loop:
    data = connection.readline().decode().strip()
    if data:
        file.write(f"{data}\n")
        while data:
            data = connection.readline().decode().strip()
            file.write("{data}\n")
        file.close()
        print("Saved")
        loop = False
