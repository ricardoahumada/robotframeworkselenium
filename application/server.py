from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/<path:path>")
def static_dir(path):
    return send_from_directory("", path)

if __name__ == "__main__":
    app.run()