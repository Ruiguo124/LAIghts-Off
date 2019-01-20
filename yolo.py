import serial                                 # add Serial library for Serial communication
print("asdasdasd")
Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object called arduinoSerialData
#Arduino_Serial.readline()                      #read the serial data and print it as line
print ("Enter 1 to ON LED and 0 to OFF LED")

while 1:                                      #infinite loop
    input_data = input()                  #waits until user enters data
    print ("you entered", str(input_data))           #prints the data for confirmation
    
    if (input_data == '1'):                   #if the entered data is 1 
        Arduino_Serial.write(b'1')             #send 1 to arduino
        print ("LED ON")
       
    
    if (input_data == '0'):                   #if the entered data is 0
        Arduino_Serial.write(b'0')             #send 0 to arduino 
        print ("LED OFF")

    if (input_data == '2'):
        Arduino_Serial.write(b'2')
        print ("LED LEVEL 2")

    if (input_data == '3'):
        Arduino_Serial.write(b'3')
        print ("LED LEVEL 3")