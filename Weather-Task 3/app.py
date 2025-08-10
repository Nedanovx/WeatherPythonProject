from flask import Flask, render_template, request
from Weather import get_five_cities, search_city

app = Flask(__name__)

@app.route("/")
def home():
    cities = get_five_cities()
    return render_template("index.html", cities=cities)

if __name__ == "__main__":
    app.run(debug=True)