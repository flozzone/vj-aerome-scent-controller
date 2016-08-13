import logging.config
import signal

from flask import Flask, send_from_directory
from flask.ext.socketio import SocketIO

from aerome_scent_controller import AeromeScentController


SERIAL_PORT = "TODO"


# Instanciate Flask (Static files and REST API)
app = Flask(__name__)
# Instanciate SocketIO (Websockets, used for events) on top of it
socketio = SocketIO(app)

scent_ctrl = AeromeScentController(SERIAL_PORT)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory('static/', path)


@socketio.on('activate', namespace='/scent')
def activate_scent(valve_id):
    logging.info("Got activate for valve: " + valve_id)
    scent_ctrl.open_valve(int(valve_id))


@socketio.on('deactivate', namespace='/scent')
def dectivate_scent(valve_id):
    scent_ctrl.close_valve(int(valve_id))


def sig_term_handler(signum, frame):
    raise KeyboardInterrupt('Signal %i receivied!' % signum)


def main():
    # Initialize logger
    logging.config.fileConfig('log.ini')

    scent_ctrl.initialize_controller()

    try:
        # Set signal handler for Shutdown
        signal.signal(signal.SIGTERM, sig_term_handler)

        # Blocking! - Start Flask server
        socketio.run(app, host='0.0.0.0')
    except KeyboardInterrupt:
        pass
    finally:
        logging.error("Cleanup done, exiting")


if __name__ == '__main__':
    main()
