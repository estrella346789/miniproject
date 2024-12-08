from flask import Flask, render_template
import time
import ledandbutton
import camera
import ultrasonic

app = Flask(__name__)

def process_button_press():
    # Logic to handle button press
    # This is where you can trigger the camera, detect faces, and update the web                                     page

@ app.route('/')
def index():
    # Render the HTML template with dynamic content
    return render_template('index.html', num_people=0, message="출근/출석 시스템                                     입니다...")

if __name__ == '__main__':
    ledandbutton.init(process_button_press)
    camera.init()
    ultrasonic.init()

    try:
        while True:
            distance = ultrasonic.measureDistance()
            if distance < 50:  # Adjust this distance based on your requirements
                ledandbutton.check_button_status()
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass
    finally:
        camera.final()
        ledandbutton.cleanup()
        ultrasonic.cleanup()