from time import sleep
from SX127x.LoRa import *
from SX127x.board_config import BOARD
import RPi.GPIO as GPIO
import spidev

BOARD.setup()
#def __init__(self, verbose=True, do_calibration=False, calibration_freq=434):
class LoRaRcvCont(LoRa):
    def __init__(self, verbose=False):
        super(LoRaRcvCont, self).__init__(verbose)
        #self.set_mode(MODE.SLEEP)
        #self.set_dio_mapping([0] * 6)

    def on_rx_done(self):
        print("\nReceived: ")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print(bytes(payload).decode("utf-8",'ignore'))
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT) 

BOARD.setup()
lora = LoRaRcvCont(verbose=False)
lora.set_mode(MODE.STDBY)


def start():
    lora.reset_ptr_rx()
    lora.set_mode(MODE.RXCONT)
    #lora.on_rx_done()
    #lora.enable_irq(lora.IRQ_RX_DONE)
    while True:
        sleep(.5)
        rssi_value = lora.get_rssi_value()
        status = lora.get_modem_status()
        sys.stdout.flush()
            






#  Medium Range  Defaults after init are 434.0MHz, Bw = 125 kHz, Cr = 4/5, Sf = 128chips/symbol, CRC on 13 dBm
lora.set_pa_config(pa_select=1)

try:
    start()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("")
    lora.set_mode(MODE.SLEEP)
    BOARD.teardown()
