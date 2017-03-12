#!/usr/bin/env python2

import logging.config
import signal

from flask import Flask, send_from_directory, jsonify
from flask_socketio import SocketIO

from gpio_stinkomat_6000_controller import AeromeScentController


SERIAL_PORT = "TODO"
SCENT_DURATION_SEC = 1


# Instanciate Flask (Static files and REST API)
app = Flask(__name__)
# Instanciate SocketIO (Websockets, used for events) on top of it
socketio = SocketIO(app)
# Instanciate Scent controller
scent_ctrl = AeromeScentController(SERIAL_PORT)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static/', path)


@app.route('/status', methods=['GET'])
def get_staus():
    return jsonify(scent_ctrl.get_state())


def close_valve_task(valve_id, duration=SCENT_DURATION_SEC):
    socketio.sleep(duration)
    scent_ctrl.close_valve(valve_id)


def state_changed_callback():
    logging.info('Execute state changed callback ...')
    socketio.emit('status_changed', scent_ctrl.get_state(), namespace='/scent')


@socketio.on('activate', namespace='/scent')
def activate_scent(valve_id):
    logging.info("Got activate for valve: %s" % valve_id)
    scent_ctrl.open_valve(valve_id)
    socketio.start_background_task(close_valve_task, valve_id)


@socketio.on('deactivate', namespace='/scent')
def deactivate_scent(valve_id):
    logging.info("Got deactivate for valve: %s" % valve_id)
    scent_ctrl.close_valve(valve_id)


@socketio.on('deactivateAll', namespace='/scent')
def deactivate_all_scents(_=None):
    logging.info("Got deactivate for all valves")
    scent_ctrl.close_all_valves()


def sig_term_handler(signum, frame):
    raise KeyboardInterrupt('Signal %i receivied!' % signum)


def main():
    # Initialize logger
    logging.config.fileConfig('log.ini')

    scent_ctrl.initialize_controller(state_changed_callback)

    try:
        # Set signal handler for Shutdown
        signal.signal(signal.SIGTERM, sig_term_handler)

        # Blocking! - Start Flask server
        socketio.run(app, host='0.0.0.0')
    except KeyboardInterrupt:
        scent_ctrl.close()
    finally:
        logging.error("Cleanup done, exiting")


if __name__ == '__main__':
    main()
