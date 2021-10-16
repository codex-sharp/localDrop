from flask import Flask
from flask import request
from flask import send_file
from utils import *

app = Flask(__name__)

@app.route('/')
def downloadFile ():
    url = request.url
    fpath = get_file_path(url)
    return send_file(fpath, as_attachment=True)

if __name__ == '__main__':
    app.run(port=5000,debug=True) 