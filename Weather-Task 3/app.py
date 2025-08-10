from flask import Flask, render_template,request
from Weather import get_five_cities,search_city

app = Flask(__name__)

@app.route("/")
def home():
    cities = get_five_cities()
    return render_template("index.html", cities=cities)

@app.route("/search")
def search():
    city_name = request.args.get("city")
    city_data = search_city(city_name)

    if not city_data:
        return render_template("error.html", error=f"City '{city_name}' not found"), 404

    return render_template("city.html", city=city_data)

if __name__ == "__main__":
    app.run(debug=True)