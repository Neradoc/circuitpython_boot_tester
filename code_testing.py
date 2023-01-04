import board
import time
from digitalio import *

OUTPUT_PIN = board.RX

output = DigitalInOut(OUTPUT_PIN)
output.switch_to_output(False)

# on ESP we set it low then high,
# because they might be set high earlier during board reset.

time.sleep(0.001)
output.value = True

while True:
    pass
