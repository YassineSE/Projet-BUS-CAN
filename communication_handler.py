import sys
from can_interface import CANInterface, CAN_Message
import time

ID_1 = 1

class CommunicationHandler:
    def __init__(self):
        # CAN interface initialization
        self.can_interface = CANInterface(channel='can0')
        self.wind_speed = 0
        self.pressure = 0
        self.temperature = 0
        self.humidity = 0      

    def send_motor_speed(self, speed):
        # Prepare message with ID = 1 and data = [speed]
        message = CAN_Message(
            id=ID_1,               # Message ID
            data=[3, speed],    # Data, here the speed value
            length=2,           # Data length
            format=0,           # Standard format (11 bits)
            type=0              # Data Frame
        )
        self.can_interface.send_message(message)

    def get_wind_speed(self):
        # Prepare message to request wind speed with ID = 1 and data = [1]
        message = CAN_Message(
            id=ID_1,               # Message ID
            data=[1],           # Data, requesting wind speed
            length=1,           # Data length
            format=0,           # Standard format (11 bits)
            type=0              # Data Frame
        )
        self.can_interface.send_message(message)
        msg = self.can_interface.receive_message()  # Receive a message
        if msg:
            # Update HMI labels based on message ID
            if msg.id == 0x55:  # Wind speed
                self.wind_speed = msg.data[0] 
                print('Wind speed: ' + str(self.wind_speed))

    def send_motor_mode(self, manual_mode):
        # Prepare message to set motor mode (manual/auto) with ID = 1
        message = CAN_Message(
            id=ID_1,               # Message ID
            data=[2, manual_mode],  # 1 for manual, 0 for auto
            length=2,           # Data length
            format=0,           # Standard format (11 bits)
            type=0              # Data Frame
        )
        self.can_interface.send_message(message)

    def get_pres_hum_temp_dist_lum_measurements(self):
        # Send CAN message with ID=2 requesting measurements
        message = CAN_Message(
            id=2,               # Message ID
            data=[1],           # Command to request measurements
            length=1,           # Data length
            format=0,           # Standard format (11 bits)
            type=0              # Data Frame
        )
        self.can_interface.send_message(message)

        # Receive the CAN message with sensor data
        msg = self.can_interface.receive_message()

        if msg and msg.id == 0x56:  # Verify the message is valid
            # Extract measurements from the received data
            press_int = (msg.data[0] << 8) | msg.data[1]  # Pressure (16 bits)
            hum_int = (msg.data[2] << 8) | msg.data[3]    # Humidity (16 bits)
            temp_int = (msg.data[4] << 8) | msg.data[5]   # Temperature (16 bits)
            dist_int = msg.data[6]                        # Distance (8 bits)
            # Light or other data may be in msg.data[7]

            # Convert the measurements from integers to real values
            self.pressure = press_int / 1.0  # Convert to hPa
            self.humidity = hum_int / 100.0  # Convert to %
            self.temperature = temp_int / 100.0  # Convert to °C
            self.distance = dist_int  # Already in a suitable scale

            # Display the values for debugging
            print(f"Pressure: {self.pressure} hPa, Humidity: {self.humidity} %, "
                  f"Temperature: {self.temperature} °C, Distance: {self.distance} cm")


if __name__ == '__main__':
    handler = CommunicationHandler() 
    speed = 50
    print('Auto mode')
    time.sleep(5)
    handler.send_motor_speed(speed)
    handler.send_motor_mode(1)  # Switch to manual mode
    print('Manual mode')
    time.sleep(5)
    handler.send_motor_mode(0)  # Switch back to auto mode
    print('Auto mode')
    while True:
        handler.get_wind_speed()
