import os
import subprocess
from enum import Enum

from exceptions import GpioError


class PinMode(Enum):
    INPUT = 'input'
    OUTPUT = 'output'


class PinValue(Enum):
    ON = 1
    OFF = 0


class GPIO:
    """Class, that contains static methods to control GPIO pins"""

    @staticmethod
    def change_pin_mode(pin: int, mode: PinMode):
        """Change GPIO pin mode. Mode is represented as gpio.PinMode enum"""
        os.system('gpio mode {pin} {mode}'.format(pin=pin, mode=mode.value))

    @staticmethod
    def write_to_pin(pin: int, value: PinValue):
        """
        Change GPIO pin value.
        Pin value is represented with gpio.PinValue enum.
        To use this func set pin to gpio.PinMode.OUTPUT mode first.
        """
        os.system('gpio write {pin} {value}'.format(pin=pin, value=value.value))

    @staticmethod
    def read_pin(pin: int) -> int:
        """Read GPIO pin value""" 
        output = subprocess.check_output('gpio read {pin}'.format(pin=pin), shell=True)
        try:
            return int(output)
        except ValueError:
            raise GpioError('Failed to read pin. Pi output is "{output}"'.format(output=output))

