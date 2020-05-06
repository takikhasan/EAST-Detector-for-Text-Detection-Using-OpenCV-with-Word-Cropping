import os
import shutil
import urllib.request
from flask import Flask, request, redirect, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_ngrok import run_with_ngrok


UPLOAD_FOLDER = 'images'
DOWNLOAD_FOLDER = 'static'

app = Flask(__name__)
run_with_ngrok(app)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024


@app.route('/', methods=['GET','POST'])
def upload_file():
    # delete folders
    try:
        shutil.rmtree(UPLOAD_FOLDER)
    except Exception as e:
        do = "nothing"
    try:
        shutil.rmtree(DOWNLOAD_FOLDER)
    except Exception as e:
        do = "nothing"

    # create empty output folders
    uncreated = 1
    while (uncreated):
        try:
            os.mkdir(UPLOAD_FOLDER)
            uncreated = 0
        except Exception as e:
            do = "nothing"
    uncreated = 1
    while (uncreated):
        try:
            os.mkdir(DOWNLOAD_FOLDER)
            uncreated = 0
        except Exception as e:
            do = "nothing"
            
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message' : 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        else:
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.jpg'))
            # resp = jsonify({'message' : 'File successfully uploaded'})
            # resp.status_code = 201
            os.system('python speech.py')
            return send_from_directory(DOWNLOAD_FOLDER, 'result.wav', as_attachment=True)

if __name__ == "__main__":
    app.run()


