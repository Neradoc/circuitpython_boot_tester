from digitalio import *
import board
from supervisor import ticks_ms

rx = DigitalInOut(board.RX)
rx.pull = Pull.DOWN
tx = DigitalInOut(board.TX)
tx.pull = Pull.DOWN

power = DigitalInOut(board.A2)
power.pull = Pull.DOWN

previous = (rx.value, tx.value)
past = ticks_ms()

power_past = False

while True:
	now = ticks_ms()

	current = (rx.value, tx.value)
	if current != previous:
		show = False
		if current[0] and current[0] != previous[0]:
			print("RX changed ", end="")
			show = True
		if current[1] and current[1] != previous[1]:
			print("TX changed ", end="")
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

