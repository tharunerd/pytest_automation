import requests

def test_weather_api():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m")
    assert response.status_code == 200
    assert "hourly" in response.json()