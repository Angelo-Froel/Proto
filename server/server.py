from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/')
def handle_packet():
    packet = request.remote_addr + ': ' + str(time.time())
    return packet

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
