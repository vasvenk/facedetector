from flask import Flask, request, jsonify
import numpy as np

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/faces', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....


    resp = jsonify(success=True)
    return resp


# start flask app
app.run()
