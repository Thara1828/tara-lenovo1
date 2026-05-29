from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select")
def select():
    return render_template("select.html")

@app.route("/support")
def support():
    return render_template("support.html")

if __name__ == "__main__":
    app.run(debug=True)
