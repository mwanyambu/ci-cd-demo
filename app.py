from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    # Reads the version dynamically from version.txt
    with open("version.txt") as f:
        version = f.read().strip()
    return render_template("index.html", version=version)

if __name__ == "__main__":
    app.run(debug=True)

