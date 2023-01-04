# Test the timing of Circuitpython boot

- connect the 3V output of the tested board to a pin on the tester board.
- connect some output pin from the tested board to the tester board for `code.py`.
- connect some output pin from the tested board to the tester board for `boot.py`.
- install `code_testing.py` as `code.py` on the tested board.
- install `boot_testing.py` as `boot.py` on the tested board.
- install `boot_tester.py` as `code.py` on the tester board.
- connect to the REPL of the tester board.
- eject the tested board drive.
- turn off poser to the tested board (typically unplug it) and back on.

Note that the time to get to code.py is increased if there is a boot.py, as it not only run but requires bringing up and down it's own python Virtual Machine. I measured an average of 32ms between them on RP2040.

Also note that `code.py` might run twice if the tested board is powered by a PC data USB, depending on the OS, since some will do something to the disk causing an autoreload some time after it mounts.

You can use a power-only cable for the tested board, though I didn't get different timings despite the USB enumeration time. Since USB is not necessarily fully ready when code.py starts, that might be because it's done in parallel.

# Test results

In the files I connected power to A2, TX to TX and RX to RX.
On the MagTag I used the Stemma QT port for power, SDA and SCL for output pins.
Originally tested with a Feather M4 as the testing board.

The times reported here are for `code.py`, the `boot.py` pin was not used.

Feather RP2040 (8.0.0 beta 6).
- 1328 ms to start `code.py`.
- 328 ms to start `code.py` with the safe mode wait disabled.

Magtag (8.0.0 beta 6).
- 2450 ms to start `code.py` (including tinyuf2 and safe mode).
- 1450 ms to start `code.py` with the safe mode wait disabled.
- 985 ms to start `code.py` without tinyuf2 and safe mode.

# Modes

Disabling safe mode is done by adding this line in `mpconfigboard.h`.
```c
#define CIRCUITPY_SKIP_SAFE_MODE_WAIT (1)
```
