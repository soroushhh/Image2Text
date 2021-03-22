from flask import render_template, request, redirect, url_for, flash
from flask import jsonify
from flaskapp import app
from flaskapp.transform import transform_image_to_text


ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            text = transform_image_to_text(file)
            return render_template("index.html", text=text)
        else:
            return render_template("index.html", error="Something Went Wrong")

    else:
        return render_template("index.html")
