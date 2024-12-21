from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# URL checking route
@app.route('/check', methods=['POST'])
def check_url():
    url = request.form['url']
    try:
        # Check if the URL is reachable
        response = requests.get(url)
        status = response.status_code
        return render_template('index.html', url=url, status=status)
    except requests.exceptions.RequestException as e:
        return render_template('index.html', url=url, status="Invalid URL or unreachable")

if __name__ == '__main__':
    app.run(debug=True)