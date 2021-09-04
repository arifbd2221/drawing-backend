from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('canvas-data')
def handle_canvas_data(data):
    print('received message: ', data)
    emit('canvas-data', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)