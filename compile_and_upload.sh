

#!/bin/bash
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -t|--target) TARGET="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

BOARD=arduino:avr:uno
PORT=/dev/tty.usbmodem1201
arduino-cli compile -b $BOARD \
-u \
-p $PORT \
./modbus/$TARGET/$TARGET.ino