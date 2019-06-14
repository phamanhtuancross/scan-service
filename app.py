import  SheetVision.main as sheetvesion
from flask import Flask,jsonify
app = Flask(__name__)

sheetvesion.scan_image_to_json_object("Users/phamanhtuan/Desktop/me/school-project/midi-team/back-end/scan-service/SheetVision/resources/samples/fire.jpg")


@app.route('/')
def root():
    return 'Hello World!'

@app.route('/scan')
def scan_image():


    return jsonify(
        success = True,
        data = "12345"
    )



if __name__ == '__main__':
    app.run()
