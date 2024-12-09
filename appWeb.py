from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html', ViewData={"Title": "Aplicacion Web 2"})

# Evento para manejar el mensaje enviado desde el cliente
@socketio.on('send_message')
def handle_send_message(message):
    print(f'Mensaje recibido del cliente: {message}')
    # Enviar respuesta al cliente
    socketio.emit('response', 'Mensaje recibido correctamente')

if __name__ == "__main__":
    # Usar SocketIO para iniciar el servidor
    socketio.run(app, host="0.0.0.0", port=5000)