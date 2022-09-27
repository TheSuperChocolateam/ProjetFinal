from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
from flux import flux

app = Flask(__name__)

import sys
import os

@app.route('/', methods=['GET', 'POST'])
def menu():
    entry=flux() 
    return render_template("index.html", entry=entry)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)