from math import exp

def fuel_agent(payload_mass: float, delta_v: float, isp: float, g0: float = 9.80665) -> dict:
    """
    Fuel Agent:
    Calculates required propellant mass using the Tsiolkovsky Rocket Equation.

    Parameters:
        payload_mass (float): Final spacecraft mass after fuel is burned (kg)
        delta_v (float): Required change in velocity (m/s)
        isp (float): Specific impulse of the engine (s)
        g0 (float): Gravitational acceleration constant (default 9.80665 m/s²)

    Returns:
        dict: {
            'delta_v_required_m_per_s': float,
            'specific_impulse_s': float,
            'payload_mass_kg': float,
            'propellant_mass_kg': float,
            'initial_mass_kg': float,
            'propellant_percentage': float
        }
    """
    mass_ratio = exp(delta_v / (isp * g0))
    initial_mass = payload_mass * mass_ratio
    propellant_mass = initial_mass - payload_mass

    return {
        'delta_v_required_m_per_s': round(delta_v, 2),
        'specific_impulse_s': round(isp, 2),
        'payload_mass_kg': round(payload_mass, 2),
        'propellant_mass_kg': round(propellant_mass, 2),
        'initial_mass_kg': round(initial_mass, 2),
        'propellant_percentage': round((propellant_mass / initial_mass) * 100, 2)
    }

# 🚀 Example Usage
if __name__ == "__main__":
    result = fuel_agent(
        payload_mass=1000,     # in kg
        delta_v=9500,          # in m/s, typical for LEO mission
        isp=350                # in seconds, cryogenic engine
    )

    print("🚀 Fuel Agent Output:")
    for key, value in result.items():
        print(f"{key}: {value}")
