import serial
import binascii
import pymongo
from pymongo import MongoClient
import datetime


# Database of registered users

# There is one database containing 2 collections
client = MongoClient('localhost', 27017)
db = client['appdb']

#collections are for newUsers and registeredUsers
collection_1 = db['registeredUsers']
collection_2 = db['newUsers']

# Reading RFID tags from reader
# Configure the COM port settings
com_port = 'COM3'  # Change this to the COM port you're using
baud_rate = 57600  # Change this to match your device's baud rate
timeout = 1  # Set a timeout for reading (in seconds)

# Current entry and exit date and time
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
date, time = formatted_datetime.split(' ')
Total_tags = []
count = 0

try:
    # Open the COM port
    ser = serial.Serial(com_port, baud_rate, timeout=timeout, bytesize=8)
    print(f"Connected to {com_port} at {baud_rate} baud")

    while True:
        # Read data from the COM port
        #data = ser.readline().decode('iso-8859-1')  # Change the encoding as needed
        data = binascii.hexlify(ser.readline())
        
        # Process and decode the received data here
        #  Print the received data
        tagID = str(data.strip())[20:-5]
        print("Received:", tagID)
        Total_tags.append(tagID)
        count += 1


except serial.SerialException as e:
    print("Serial port error:", e)

#When ctrl + c is pressed in terminal program terminated
except KeyboardInterrupt:
    print("Keyboard interrupt. Closing the COM port.")
    ser.close()


# Number of times the RFID reads tags
print("Tags captured= ", Total_tags)
print ("count = ", count)
print("Entry date: ", date)
print("Entry time: ", time)
processed_tags = set()

# updating entry date and time
new_fields = {
    "Entry_Date": date,
    "Entry_Time": time
}

# Updating database when user entered carpark
for tag in Total_tags:
    if tag not in processed_tags:
        if len(tag) < 30 and tag != "":
            match_success = collection_1.find({"RFID": tag})
            processed_tags.add(tag)
            

            if match_success:
                collection_1.update_one({"RFID": tag},  {"$set": new_fields})      
                print("User Found")
                print("User updated with Entry time/date")
 

