# Test the timing of Circuitpython boot

- connect the 3V output of the tested board to a pin on the testing board
- connect some output pin from the tested board to the testing board

In the files I conencted power to A2 and SDA to RX.
Originally tested with a Feather M4 as the testing board.

Feather RP2040:
- 1320 ms boot time (including safe mode)

Magtag:
- 2450 ms boot time (including tinyuf2 and safe mode)
- 1450 ms boot time without safe mode
- 985 ms without tinyuf2 and safe mode
