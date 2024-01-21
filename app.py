# ---------- app.py -------------------
# Basic imports
from flask import Flask, request,render_template, redirect, url_for

# Imports Within the App
from model import get_weather_data

# Instantiating the Flask Application
app = Flask(__name__)

# Landing Main Page
@app.route('/')
def main():
    return render_template('main.html')

# Search Intermediate Page
@app.route('/search', methods=['POST'])
def search():
    city = request.form['city'].capitalize()
    return redirect(url_for('detail', city=city))

# City Weather Detailed Page
@app.route('/detail/<city>')
def detail(city):
    data = get_weather_data(city)
    return render_template('detail.html', data=data)





if __name__ == '__main__':
    app.run(debug=True)
