from flask import Flask, render_template, request

from lib.decode import decode_qr

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/decode", methods=["GET", "POST"])
def decode():
    file = request.files["file"]
    if file:
        decode = decode_qr(file)
        return render_template(
            "index.html",
            status=decode["status"],
            data=decode["data"],
            response=decode["response"],
        )
    else:
        return {"status": "error", "message": "No file provided"}


if __name__ == "__main__":
    app.run(debug=True)
