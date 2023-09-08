import serial
import binascii

# Configure the COM port settings
com_port = 'COM3'  # Change this to the COM port you're using
baud_rate = 57600  # Change this to match your device's baud rate
timeout = 1  # Set a timeout for reading (in seconds)

try:
    # Open the COM port
    ser = serial.Serial(com_port, baud_rate, timeout=timeout, bytesize=8)
    print(f"Connected to {com_port} at {baud_rate} baud")

    while True:
        # Read data from the COM port
        #data = ser.readline().decode('iso-8859-1')  # Change the encoding as needed
        data = binascii.hexlify(ser.readline())
        # Process and decode the received data here
        # Example: Print the received data

        print("Received:", str(data.strip())[20:-5])

except serial.SerialException as e:
    print("Serial port error:", e)

except KeyboardInterrupt:
    print("Keyboard interrupt. Closing the COM port.")
    ser.close()
