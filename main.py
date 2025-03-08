import os
from flask import Flask, redirect, render_template, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def login():
    return render_template('main.html')


@app.route('/second')
def second():
    return render_template('second.html')


@socketio.on('red')
def smoke():
    emit('redirect', {'url': url_for('second')})


if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.urandom(12)
    socketio.run(app, host='0.0.0.0', port=4444, allow_unsafe_werkzeug=True)
