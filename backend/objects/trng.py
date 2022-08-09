from serial import Serial
from serial.tools.list_ports import comports

TRNG_CHAR = b't'
COUNT_CHAR = b'c'
IDLE_CHAR = b'i'

class Trng():
    def __init__(self) -> None:
        pass

    def setUp(self):
        for port in comports():
            if port.description == 'μacm':
                device = port.device
        assert device, 'muacm device not found'
        self.ser = Serial(device, timeout=3)
        if not self.ser.is_open:
            self.ser.open()

    def start_trng(self):
        self.ser.write(TRNG_CHAR)

    def start_count(self):
        self.ser.write(COUNT_CHAR)

    def read_trng(self, amount_bytes: int) -> bytes:
        result = self.ser.read_until('', amount_bytes)
        return result
    
    def stop(self):
        self.ser.write(IDLE_CHAR)

    def next(self):
        return int.from_bytes(self.read_trng(4), "big") 


