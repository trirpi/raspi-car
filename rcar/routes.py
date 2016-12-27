from flask import render_template
from flask_socketio import SocketIO

from rcar import app
from car import Car

socketio = SocketIO(app)
rob = Car()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message')
def drive(message):
    if message['data'] == 'forward':
        rob.drive_forwards()
    elif message['data'] == 'backward':
        rob.drive_backwards()
    elif message['data'] == 'left':
        rob.turn_left()
    elif message['data'] == 'right':
        rob.turn_right()
    elif message['data'] == 'stop':
        rob.stop()
    elif message['data'].split()[0] == "speed":
        rob.set_speed(message['data'].split[1])
    else:
        print(message['data'])

if __name__ == '__main__':
    socketio.run(app)
