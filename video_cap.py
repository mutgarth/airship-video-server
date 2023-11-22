import cv2

class VideoCap():
    
    def __init__(self, cam_id) -> None:

        self.camera_name = 'camera'+str(cam_id)+'.jpg'
        self.camera = cv2.VideoCapture(cam_id) 

    def generate(self):
        while True:
            _, frame = self.camera.read()
            _, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')