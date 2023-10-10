from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__, template_folder="template")

UPLOAD_FOLDER = os.path.join(os.getcwd(),'C:/Users/User/Downloads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['meuArquivo']
    savePath = os.path.join (UPLOAD_FOLDER, secure_filename(file.filename))
    file.save  (savePath)
    return 'Upload feito com sucesso' 


if __name__ == "__main__":
    app.run(debug=True)
