from flask import Flask, Response
from video_cap import VideoCap

app = Flask(__name__)

cam1 = VideoCap(0)
cam2 = VideoCap(1)

@app.route('/stream1')
def stream1():
    return Response(cam1.generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stream2')
def stream2():
    return Response(cam2.generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, threaded=True)