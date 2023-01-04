from digitalio import *
import board
from supervisor import ticks_ms

POWER_PIN = board.A2
BOOT_PIN = board.TX
CODE_PIN = board.RX

boot_status = DigitalInOut(BOOT_PIN)
boot_status.pull = Pull.DOWN
code_status = DigitalInOut(CODE_PIN)
code_status.pull = Pull.DOWN

power = DigitalInOut(POWER_PIN)
power.pull = Pull.DOWN

previous = (boot_status.value, code_status.value)
past = ticks_ms()

power_past = False

while True:
	now = ticks_ms()

	current = (boot_status.value, code_status.value)
	if current != previous:
		show = False
		if current[0] and current[0] != previous[0]:
			print("boot.py pin changed ", end="")
			show = True
		if current[1] and current[1] != previous[1]:
			print("code.py pin changed ", end="")
			show = True
		if show:
			print(f"{now - past} ms") # f" {current}")
		past = now
		previous = current

	if power.value != power_past:
		if power.value:
			print("Power on") # , now - past)
		else:
			print("Power off") # , now - past)
		past = now
		power_past = power.value

