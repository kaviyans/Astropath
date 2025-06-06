from skyfield.api import load
from datetime import datetime, timedelta
import numpy as np

def launch_window_agent(source_planet: str, target_planet: str, 
                        start_date: str, end_date: str, 
                        threshold_deg: float = 3.0) -> dict:
    """
    Launch Window Agent:
    Finds the best launch dates between two planets when angular separation is optimal.

    Parameters:
        source_planet (str): The starting planet (e.g., "earth").
        target_planet (str): The destination planet (e.g., "mars").
        start_date (str): Start of mission planning window in "YYYY-MM-DD".
        end_date (str): End of mission planning window in "YYYY-MM-DD".
        threshold_deg (float): Angular separation threshold (in degrees) for optimal launch.

    Returns:
        dict: {
            'source_planet': str,
            'target_planet': str,
            'threshold_deg': float,
            'suggested_launch_dates': List[Dict[date, separation]]
        }
    """
    ts = load.timescale()
    ephemeris = load('de421.bsp')
    sun = ephemeris['sun']
    source = ephemeris[source_planet.lower()]
    target = ephemeris[target_planet.lower()]

    # Convert date strings to datetime
    start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(end_date, "%Y-%m-%d")
    days_range = (end_dt - start_dt).days

    # Generate time range
    dates = [start_dt + timedelta(days=i) for i in range(days_range)]
    times = ts.utc([d.year for d in dates], [d.month for d in dates], [d.day for d in dates])

    # Calculate angular separation for each day
    launch_dates = []
    for t in times:
        angle = sun.at(t).observe(source).apparent().separation_from(
                sun.at(t).observe(target).apparent()).degrees
        if angle < threshold_deg:
            launch_dates.append({
                'date': str(t.utc_datetime().date()),
                'angular_separation_deg': round(angle, 2)
            })

    return {
        'source_planet': source_planet.title(),
        'target_planet': target_planet.title(),
        'threshold_deg': threshold_deg,
        'suggested_launch_dates': launch_dates or "No optimal windows found in this range."
    }

if __name__ == "_main_":
    result = launch_window_agent(
        source_planet="Earth",
        target_planet="Mars",
        start_date="2026-01-01",
        end_date="2027-12-31",
        threshold_deg=3.0
    )
    print(result)