from flask import Flask, request, jsonify
import numpy as np

# Initialize the Flask application
app = Flask(__name__)
numPics = 0

# route http posts to this method
@app.route('/faces', methods=['POST'])
def test():
    r = request
    

    f = open('/home/nvidia/pics/img%s.jpg' % numPics, 'wb')
    f.write(request.data)
    f.close()
    numPics += 1
    # do some fancy processing here....

    resp = jsonify(success=True)
    return resp

# start flask app
app.run(host= '0.0.0.0')
