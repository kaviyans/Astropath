from datetime import datetime
import requests

def weather_agent(city: str, date: str, api_key: str) -> dict:
    """
    Parameters:
        city (str): City name (e.g., "Chennai", "Cape Canaveral")
        date (str): Date in "YYYY-MM-DD" format
        api_key (str): OpenWeatherMap API key

    Returns:
        dict: {
            'city': str,
            'launch_date': str,
            'cloud_cover': float (%),
            'wind_speed': float (m/s),
            'description': str,
            'launch_recommendation': str
        }
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()

        target_date = datetime.strptime(date, "%Y-%m-%d").date()

        closest_forecast = None
        for entry in data.get("list", []):
            forecast_time = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
            if forecast_time.date() == target_date:
                closest_forecast = entry
                break

        if not closest_forecast:
            return {"error": "Weather forecast not available for the specified date."}

        clouds = closest_forecast["clouds"]["all"]
        wind_speed = closest_forecast["wind"]["speed"]
        description = closest_forecast["weather"][0]["description"]

        if clouds > 80 or wind_speed > 15:
            recommendation = "❌ Launch not recommended due to weather conditions."
        else:
            recommendation = "✅ Weather is acceptable for launch."

        return {
            "city": city,
            "launch_date": date,
            "cloud_cover": clouds,
            "wind_speed": wind_speed,
            "description": description,
            "launch_recommendation": recommendation
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "main":
    api_key = "YOUR_API_KEY" # Replace with your OpenWeatherMap API key
    output = weather_agent(city="Chennai", date="2025-06-10", api_key=api_key)
    for k, v in output.items():
        print(f"{k}: {v}")