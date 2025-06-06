from skyfield.api import load
import numpy as np
from datetime import datetime

def trajectory_agent(source_planet: str, target_planet: str, departure_date: str) -> dict:
    """
    Trajectory Agent:
    Computes a Hohmann transfer trajectory between two planets using Skyfield.

    Parameters:
        source_planet (str): Starting planet (e.g., 'earth')
        target_planet (str): Destination planet (e.g., 'mars')
        departure_date (str): Launch date in 'YYYY-MM-DD' format

    Returns:
        dict: {
            'source': str,
            'target': str,
            'departure_date': str,
            'hohmann_transfer_time_days': float,
            'delta_v_total_km_s': float,
            'delta_v_departure_km_s': float,
            'delta_v_arrival_km_s': float,
            'semi_major_axis_km': float,
            'r1_km': float,
            'r2_km': float
        }
    """
    # Constants
    AU_KM = 149597870.7  # 1 Astronomical Unit in km
    mu_sun = 1.32712440018e11  # Gravitational parameter of the Sun in km^3/s^2

    # Load planetary ephemerides and time scale
    ephemeris = load('de421.bsp')
    ts = load.timescale()

    # Parse input date
    try:
        dt = datetime.strptime(departure_date, "%Y-%m-%d")
        t = ts.utc(dt.year, dt.month, dt.day)
    except ValueError:
        raise ValueError("Invalid departure date format. Use 'YYYY-MM-DD'.")

    # Get planets
    source = ephemeris[source_planet.lower()]
    target = ephemeris[target_planet.lower()]

    # Heliocentric distance in AU → convert to km
    r1 = source.at(t).observe(ephemeris['sun']).distance().au * AU_KM
    r2 = target.at(t).observe(ephemeris['sun']).distance().au * AU_KM

    # Hohmann semi-major axis
    a = (r1 + r2) / 2

    # Transfer time (half orbital period)
    t_sec = np.pi * np.sqrt(a**3 / mu_sun)
    t_days = t_sec / (60 * 60 * 24)

    # Orbital speeds
    v1 = np.sqrt(mu_sun / r1)  # circular at r1
    v2 = np.sqrt(mu_sun / r2)  # circular at r2
    v_trans1 = np.sqrt(2 * mu_sun * r2 / (r1 * (r1 + r2)))
    v_trans2 = np.sqrt(2 * mu_sun * r1 / (r2 * (r1 + r2)))

    delta_v1 = abs(v_trans1 - v1)
    delta_v2 = abs(v2 - v_trans2)
    delta_v_total = delta_v1 + delta_v2

    return {
        'source': source_planet.title(),
        'target': target_planet.title(),
        'departure_date': departure_date,
        'hohmann_transfer_time_days': round(t_days, 2),
        'delta_v_total_km_s': round(delta_v_total, 4),
        'delta_v_departure_km_s': round(delta_v1, 4),
        'delta_v_arrival_km_s': round(delta_v2, 4),
        'semi_major_axis_km': round(a, 2),
        'r1_km': round(r1, 2),
        'r2_km': round(r2, 2)
    }

# Example usage
if __name__ == "__main__":
    result = trajectory_agent("earth", "mars", "2026-10-12")
    print(result)
