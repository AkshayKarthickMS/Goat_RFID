# -*- coding: utf-8 -*-
import serial
from serial.tools import list_ports
import time

def detect_serial_port():
    ports = list_ports.comports()
    for port in ports:
        if 'usbmodem' in port.device or 'COM' in port.device:  # Adjust this condition based on your platform
            return port.device
    return None

def read_rfid():
    ser = None
    try:
        port = detect_serial_port()
        if not port:
            print("No RFID reader found.")
            return
        ser = serial.Serial(port, 9600)  # Adjust baud rate if necessary
        while True:
            if ser.in_waiting > 0:
                tag = ser.readline().decode('utf-8').strip()
                with open("rfid_tag.txt", "w") as file:
                    file.write(tag)
                print(f"Read RFID tag: {tag}")
            time.sleep(1)
    except serial.SerialException as e:
        print(f"SerialException: {e}")
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        if ser is not None and ser.is_open:
            ser.close()
            print("Serial port closed")

if __name__ == "__main__":
    read_rfid()
