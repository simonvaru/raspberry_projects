import time
import board
import busio
import digitalio
import adafruit_blinka  # Replace with your LoRa library
from SX127x.LoRa import *
from SX127x.board_config import BOARD

# (Replace with your LoRa configuration, adjust SPI pins if needed)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D24)
#spi = busio.SPI(BOARD.SCK, BOARD.MOSI, BOARD.MISO)
#cs = digitalio.DigitalInOut(BOARD.CS)
lora1 = LoRa()
lora = lora1(spi, cs, frequency=433.0e6)
#lora = LoRa(spi, cs, BOARD.IRQ, frequency=..., bandwidth=..., spreading_factor=...)

# (Replace with your LoRaWAN network credentials)
dev_eui = b"\x00\x00\x00\x00\x00\x00\x00\x00"
app_eui = b"\x00\x00\x00\x00\00\x00\x00\x00"
app_key = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

# LoRa configuration (adjust according to your network)
lora.set_ADR(False)
lora.set_tx_power(20, False)

def join_network():
    # Join the LoRaWAN network (replace with your credentials)
    try:
        join = lora.join(activation_type=adafruit_blinka.LORA_ACTIVATION_OTAA, dev_eui=dev_eui, app_eui=app_eui, app_key=app_key)
        print("Joined! Network confirmed:", join.confirmed)
    except RuntimeError as e:
        print("Join failed:", e)
        while True:
            pass

# Function to send LoRa message (replace "led_state" with actual state)
def send_lora_message(led_state):
    """Sends a LoRa message indicating the LED state"""
    # Replace with a message identifier or format based on your LoRaWAN network requirements
    message = f"LED State: {led_state}"

    packet = bytearray(len(message) + 4)
    packet[0] = 0x01  # Assuming message type (adjust based on your LoRaWAN setup)
    packet[1:4] = len(message).to_bytes(3, 'little')  # Payload length
    packet[4:] = message.encode()
    lora.send(packet)
    print("Sent message:", message)

def get_button_state():
    return not button_pin.value  # Button press triggers low signal

def main():
    join_network()  # Join LoRa network (from common code)

    led_state = False  # Initial LED state

    while True:
        # Check button press
        if button_pin.value != led_state:  # Button state changed
            led_state = not led_state  # Toggle LED state on button press
            led_pin.value = led_state  # Update LED based on state

            # Send LoRa message with updated LED state
            send_lora_message(led_state)

        time.sleep(0.1)  # Short delay to avoid excessive button reads

if __name__ == "__main__":
    main()