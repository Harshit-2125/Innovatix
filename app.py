from flask import Flask, render_template, url_for, redirect, request
from flask import request, jsonify

app = Flask(__name__)

API_KEY = 'XReMGBtpaMpsrNd3HSPCA'
CITY = 'Delhi'

# Function to get weather data
def get_weather_data():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = request.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data"}

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the "Call us" button
@app.route('/call_us')
def call_us():
    return redirect(url_for('home'))

# Route for the Grow Shining page
@app.route('/grow_shining')
def grow_shining():
    return render_template('grow_shining.html')

# Route for the Illuminate page
@app.route('/illuminate')
def illuminate():
    return render_template('illuminate.html')

# Route for the "Contact" button
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for Intelligent Street Monitoring form page
@app.route('/monitor_street_page')
def monitor_street_page():
    return render_template('monitor_street.html')

# Route for Smart Irrigation page
@app.route('/smart_irrigation')
def smart_irrigation_page():
    return render_template('smart_irrigation.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    # Call the chatbot API here and get the response
    response_message = call_chatbot_api(user_message)
    return jsonify({'response': response_message})

# Route for Energy Efficiency System page
@app.route('/energy_efficiency')
def energy_efficiency_page():
    # Fetch or calculate data here
    energy_efficiency = 75.5  # Example value
    co2_savings = 15.3  # Example value
    return render_template(
        'energy_efficiency.html',
        efficiency=energy_efficiency,
        co2_savings=co2_savings
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

