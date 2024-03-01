from flask import Flask, render_template, request
from weather import get_lat_lon, get_current_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateCode']
        country = request.form['countryName']
        
        lat, lon = get_lat_lon(city, state, country)
        data = get_current_weather(lat, lon)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
