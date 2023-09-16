import requests
import sqlite3
from datetime import datetime

def fetch_weather_data():
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=VALID_API_KEY&q=London')
    return response.json()

def save_weather_data_to_sqlite(weather_data):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS weather_data (date text, weather text)')
    c.execute('INSERT INTO weather_data VALUES (?, ?)', (datetime.now().strftime('%Y-%m-%d'), str(weather_data)))
    conn.commit()
    conn.close()
