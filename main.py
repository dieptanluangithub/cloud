from flask import render_template, Flask

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("test.html")
if __name__ == "__main__":
    app.run()