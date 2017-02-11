import logging
import RPi.GPIO as GPIO
from threading import Lock


# Scent valves 0 to 5
SCENT_ID_TO_PIN_MAPPING = {
    '0': 11,
    '1': 13,
    '2': 15,
    '3': 16,
    '4': 18,
    '5': 22
}
# Flush valve
FLUSH_VALVE_PIN = 12


class AeromeScentController (object):

    def __init__(self, compatibility_dummy):
        self.log = None
        self.open_valves = None
        self.state_change_lock = Lock()
        self.status_changed_callback = None

    def initialize_controller(self, status_changed_callback):
        self.log = logging.getLogger("aeromeScentController")
        self.log.error("Init GPIO controller")
        GPIO.setmode(GPIO.BOARD)
        for pin in SCENT_ID_TO_PIN_MAPPING.values():
            GPIO.setup(pin, GPIO.OUT)
        GPIO.setup(FLUSH_VALVE_PIN, GPIO.OUT)
        self.close_all_valves()
        self.status_changed_callback = status_changed_callback

    @staticmethod
    def get_state():
        ret = {}
        for pin_id, pin in SCENT_ID_TO_PIN_MAPPING.iteritems():
            ret[pin_id] = GPIO.input(pin) == GPIO.HIGH
        return ret

    def open_valve(self, valve_id):
        self._set_valve_state(valve_id, GPIO.HIGH)

    def close_valve(self, valve_id):
        self._set_valve_state(valve_id, GPIO.LOW)

    def close(self):
        self.close_all_valves()
        GPIO.cleanup()

    def close_all_valves(self):
        self.state_change_lock.acquire()
        try:
            self.log.error("Closing all")
            self._set_all_pins_low()
        finally:
            self.state_change_lock.release()

    def _set_valve_state(self, valve_id, state):
        valve_key = str(valve_id)

        if valve_key not in SCENT_ID_TO_PIN_MAPPING.keys():
            self.log.error("Unknown valve %s" % valve_key)
            return

        valve_pin = SCENT_ID_TO_PIN_MAPPING[valve_key]

        self.state_change_lock.acquire()
        try:
            self._set_pin_to_state(valve_pin, state)
        finally:
            self.state_change_lock.release()

    def _set_pin_to_state(self, pin, state):
        if GPIO.input(pin) != state:
            self.log.error("Setting " + str(pin) + " to " + str(state))
            GPIO.output(pin, state)
            if state == GPIO.HIGH:
                GPIO.output(FLUSH_VALVE_PIN, state)
                self.open_valves += 1
            else:
                self.open_valves -= 1
                if self.open_valves < 1:
                    self._set_all_pins_low()
            self.status_changed_callback()
        else:
            self.log.error("Pin " + str(pin) + " is already " + str(state))

    def _set_all_pins_low(self):
        GPIO.output(SCENT_ID_TO_PIN_MAPPING.values() + [FLUSH_VALVE_PIN], GPIO.LOW)
        self.open_valves = 0
