import board
import time
from digitalio import *

OUTPUT_PIN = board.TX

output = DigitalInOut(OUTPUT_PIN)
output.switch_to_output(False)

# On ESP we set it low then high,
# Because they might be set high earlier during board reset.

time.sleep(0.001)
output.value = True

# Note that this pin will be reset between boot and code.
