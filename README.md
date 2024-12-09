# WebSocket project in Python

This project implements a basic WebSocket server in Python using Flask and Flask-SocketIO.

## Instructions to run the project
### Prerequisites
1. Make sure you have Docker installed on your machine.
2. Clone this repository to your local machine:

   ```bash
   git clone  https://github.com/alwxav98/EA4Websocket.git
   cd  EA4Websocket
   ```

### Using Docker
1. Clone this repository to your local machine.
2. Build the Docker image with the following command:

   ```bash
   docker build -t python-websocket .
   ```

3. Run the container with:

   ```bash
   docker run -d -p 5000:5000 --name websocket-container python-websocket
   ```
4. Access the application in your browser:
- Home page: http://localhost:5000

### Testing WebSocket Functionality
1. Open the Home Page in your browser.
2. Click the "Enviar mensaje" button to send a message to the server via WebSocket.
3. The server will respond, and the message will be displayed on the page under the button.
