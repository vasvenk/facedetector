from flask import Flask, request, jsonify
import numpy as np
import os

# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/faces', methods=['POST'])
def test():
    r = request
    numPics = 0
    while os.path.isfile('/home/nvidia/pics/img%s.jpg' % numPics):
        numPics += 1
    f = open('/home/nvidia/pics/img%s.jpg' % numPics, 'wb')
    f.write(request.data)
    f.close()
    numPics += 1
    # do some fancy processing here....

    resp = jsonify(success=True)
    return resp

# start flask app
app.run(host= '0.0.0.0')
