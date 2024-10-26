from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About Us button in the Hero section
@app.route('/about_us')
def about_us():
    return render_template('about.html')

# Route for the Sign Up button in the header
@app.route('/sign_up')
def sign_up():
    return render_template('login_page.html')

# Route for Projects dropdown items
@app.route('/upload')
def upload():
    return render_template('project_1.html')

# Route for investment information
@app.route('/invest')
def invest():
    return render_template('project_2.html')


# Route for news section
@app.route('/news')
def news():
    return render_template('news.html')

# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the Grow Shining button in the CTA section
@app.route('/green energy')
def green_energy():
    return render_template('green energy.html')
@app.route('/project')
def project():
    return render_template('prjoect_1.html')

@app.route('/Stock Monitoring')
def stock():
    return render_template('Stock_marketing.html')
# Route for the Call Us button in the footer
@app.route('/call_us')
def call_us():
    return render_template('call_us.html')

# Route for the Energy Efficiency System page
@app.route('/energy_efficiency')
def energy_efficiency():
    energy_efficiency = 75.5  # Example value
    co2_savings = 15.3  # Example value
    return render_template(
        'energy_efficiency.html',
        efficiency=energy_efficiency,
        co2_savings=co2_savings
    )

# Chatbot interaction endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    response_message = call_chatbot_api(user_message)
    return jsonify({'response': response_message})

# Function to simulate chatbot API interaction
def call_chatbot_api(user_message):
    return f"Chatbot received: {user_message}"

if __name__ == '__main__':
    app.run(debug=True)
