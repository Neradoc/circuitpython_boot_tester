import board
import time
from digitalio import *

sda = DigitalInOut(board.SDA)
sda.switch_to_output(False)

# on ESP we set it low then high, because they might be set high
# earlier during board reset.

time.sleep(0.001)
sda.value = True

while True:
    pass
