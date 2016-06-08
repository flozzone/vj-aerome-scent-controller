import logging
import serial
import array


class AeromeScentController (object):
    BLOCK_BEGIN = [0x1b]
    BLOCK_END = [0x0d]
    ACTIVATE_CONTROLLER = [0xe0, 0xe1, 0xe2, 0xe3, 0x0d]
    ALL_VALVES_HOLD = [0xee, 0xef]
    FLUSH_VALVE_ON = [0x26]
    FLUSH_VALVE_OFF = [0xa6]

    SCENT_VALVE_ON = 0x40
    SCENT_VALVE_OFF = 0xC0

    def __init__(self, serial_port_name):
        self.serial_port_name = serial_port_name

    def _init_serial(self):
        self.log = logging.getLogger("aeromeScentController")
        try:
            # Init Serial port
            self.serial_port = serial.Serial(self.serial_port_name, timeout=1, baudrate=9600)
            self.serial_port.flushInput()
            self.serial_port.flushOutput()

        except OSError, error:
            self.serial_port = None
            self.log.error("Cannot initialize. Reason: %s", error)

        except serial.serialutil.SerialException, error:
            self.serial_port = None
            self.log.error("Cannot initialize. Reason: %s", error)

        self.log.debug("Serial: %s", self.serial_port)

    def initialize_controller(self):
        self._init_serial()

        self._send_block(self.ALL_VALVES_HOLD)
        self._send_message(self.ACTIVATE_CONTROLLER)
        self._send_block(self.ALL_VALVES_HOLD)

    def open_valve(self, valve_id):
        self._send_block(self.FLUSH_VALVE_ON + [self.SCENT_VALVE_ON + valve_id])

    def close_valve(self, valve_id):
        self._send_block(self.FLUSH_VALVE_OFF + [self.SCENT_VALVE_OFF + valve_id])

    def _send_block(self, block_content):
        block = []
        block += self.BLOCK_BEGIN
        block += block_content
        block += self.BLOCK_END
        self._send_message(block)

    def _send_message(self, message):
        msg_str = array.array('B', message).tostring()
        self.log.debug("Sending: " + ''.join(format(x, '02x') for x in message))
        #self.serial_port.write(msg_str)
