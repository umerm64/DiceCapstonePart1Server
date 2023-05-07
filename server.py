from flask import Flask, send_file
import os
import random
import hashlib

app = Flask(__name__)
filename = '/tmp/serverdata/random.txt'


@app.route('/')
def home():
    return 'Server', 200


@app.route('/test')
def test():
    return 'Test', 200

@app.errorhandler(404)
def not_found(e):
    return 'NOT FOUND', 404

def createFile():
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    f = open(filename, 'wb')
    bytess = [random.randint(0, 1000)%256 for i in range(1024)]
    f.write(bytes(bytess))
    f.close()

@app.route('/download_file')
def sendFile():
    return send_file(filename)

@app.route('/checksum')
def getChecksum():
    return hashlib.md5(open(filename,'rb').read()).hexdigest(), 200

if __name__ == "__main__":
    createFile()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
