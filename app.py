from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    api_key = '9cdcbade0fb14083a2d151222241510'  
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_info = {
            'city': data['location']['name'],
            'temperature': data['current']['temp_c'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
            'cloud': data['current']['cloud'],
            'description': data['current']['condition']['text'],
        }
        return render_template('index.html', weather=weather_info)
    else:
        error_message = data['error']['message']
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
