import weather_data_management
import sqlite3

def test_fetch_weather_data():
    weather_data = weather_data_management.fetch_weather_data()
    assert 'main' in weather_data
    return weather_data

def test_save_weather_data_to_sqlite(weather_data):
    weather_data_management.save_weather_data_to_sqlite(weather_data)
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM weather_data')
    assert c.fetchone() is not None
    conn.close()

if __name__ == '__main__':
    weather_data = test_fetch_weather_data()
    test_save_weather_data_to_sqlite(weather_data)
