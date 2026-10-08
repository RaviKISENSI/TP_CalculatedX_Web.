from flask import Flask, render_template
from models import Calculatrice

app = Flask(__name__)
calc = Calculatrice()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)