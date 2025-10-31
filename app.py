from flask import Flask, render_template, request
from parser import parse_resume
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["resume"]
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        data = parse_resume(file_path)
        return render_template("index.html", data=data)
    return render_template("index.html", data=None)

if __name__ == "__main__":
    app.run(debug=True)
