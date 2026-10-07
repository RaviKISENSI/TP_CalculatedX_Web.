from flask import Flask
from models import Calculatrice

app = Flask(__name__)
calc = Calculatrice()

@app.route("/")
def index():
    return "CalculatedX fonctionne !"

if __name__ == "__main__":
    app.run(debug=True, port=8000)