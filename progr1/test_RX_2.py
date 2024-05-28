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
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0] * 6)

    def on_rx_done(self):
        BOARD.led_on()
        print("\nReceived: ")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        #print(bytes(payload).decode("utf-8",'ignore'))
        print(bytes(payload).decode())
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        BOARD.led_off()
        self.set_mode(MODE.RXCONT) 


    def start(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        #lora.on_rx_done()
        #lora.enable_irq(lora.IRQ_RX_DONE)
        while True:
            sleep(.5)
            rssi_value = self.get_rssi_value()
            status = self.get_modem_status()
            sys.stdout.flush()
            sys.stdout.write("\r%d %d %d" % (rssi_value, status['rx_ongoing'], status['modem_clear']))  

lora=LoRaRcvCont(verbose=False)

lora.set_mode(MODE.STDBY)
lora.set_pa_config(pa_select=1)       

#print(lora)
#assert(lora.get_agc_auto_on()==1)

try: input("Press ENTER to start...")
except: pass



try:
    lora.start()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("")
    lora.set_mode(MODE.SLEEP)
    #print(lora)
    BOARD.teardown()

GPIO.cleanup()



            
